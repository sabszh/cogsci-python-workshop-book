# Functions and analysis pipelines

Functions give each analysis step a name, inputs, and output. This makes a long
workflow easier to read and lets you test one transformation at a time. In this
chapter we build from a small NumPy function to a pandas pipeline and use assertions
to catch assumptions before they affect later results.

A research function should make one transformation explicit and testable.

```python
import numpy as np

def compute_evoked(epochs, trial_axis=0):
    """Average a 3D epochs array over its trial dimension."""
    epochs = np.asarray(epochs)  # accept array-like input consistently

    if epochs.ndim != 3:         # fail early if dimensions are unexpected
        raise ValueError(
            "Expected a 3D array shaped trials × channels × time; "
            f"received {epochs.shape}"
        )

    return epochs.mean(axis=trial_axis)  # remove the trial dimension
```

## Inputs, outputs, and side effects

Prefer returning a new result:

```python
def remove_incorrect(trials):
    mask = trials["correct"]                 # Boolean mask for retained rows
    return trials.loc[mask].copy()            # return an independent DataFrame
```

Be careful with silent mutation: a function can change an object supplied by its
caller without making that change obvious at the call site.

```python
def remove_incorrect_in_place(trials):
    trials.drop(trials.index[~trials["correct"]], inplace=True)
```

The second function changes the caller's object and returns `None`.

<div class="live-python">
  <p><strong>Check with Python:</strong> change one value so the assertion fails, then read the final error line.</p>
  <textarea aria-label="Editable function and assertion example">def mean_rt(values):
    assert len(values) &gt; 0, &quot;No reaction times supplied&quot;
    assert all(value &gt; 0 for value in values), &quot;Reaction times must be positive&quot;
    return sum(values) / len(values)
reaction_times = [0.51, 0.62, 0.73]
print(mean_rt(reaction_times))</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Compose a pipeline

A pipeline is a sequence of named steps. Each step receives the result from the
previous step, so the full analysis can be read from raw files to a summary table.

```python
def load_trials(path):
    return pd.read_csv(path)                  # read the trial table

def clean_trials(trials):
    return (
        trials
        .dropna(subset=["reaction_time"])    # remove missing reaction times
        .query("reaction_time > 0")          # keep physically plausible values
        .copy()                               # avoid mutating the input table
    )

def summarise_participants(trials):
    return (
        trials
        .groupby(["participant", "condition"], as_index=False)  # unit of summary
        .agg(
            mean_rt=("reaction_time", "mean"),
            accuracy=("correct", "mean"),
        )
    )
```

## Assertions as executable assumptions

An `assertion` checks that a condition is true at a point in the analysis. If the
condition is true, execution continues. If it is false, Python raises an
`AssertionError` and stops at that line, showing that an assumption needs attention.

```python
assert epochs.ndim == 3                              # epochs × channels × time
assert epochs.shape[1] == len(channel_names)         # one label per channel
assert trials["reaction_time"].ge(0).all()           # no negative times
```

::::{exercise} Refactor
:label: function-refactor
Turn this repeated analysis into a function that accepts an epochs array and channel index and returns a 1D evoked signal.

```python
evoked_a = epochs_a.mean(axis=0)
channel_a = evoked_a[2]

evoked_b = epochs_b.mean(axis=0)
channel_b = evoked_b[2]
```
::::

::::{admonition} Hint
:class: dropdown
Give the function all values it needs as parameters and make the transformed
DataFrame its return value. Avoid reading or modifying a global variable.
::::

::::{solution} function-refactor
```python
def evoked_channel(epochs, channel):
    if epochs.ndim != 3:
        raise ValueError("Expected trials × channels × time")
    return epochs.mean(axis=0)[channel]
```
::::
