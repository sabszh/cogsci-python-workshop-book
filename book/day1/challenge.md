# Day 1 challenge: Epochs to evoked

Work in groups of two or three. Predict shapes before running each transformation.

## Generate the data

```python
import numpy as np

rng = np.random.default_rng(7)
n_trials, n_channels, n_times = 60, 8, 300

epochs_a = rng.normal(0, 1, size=(n_trials, n_channels, n_times))
epochs_b = rng.normal(0, 1, size=(n_trials, n_channels, n_times))

# Add a condition effect to channel 2 between samples 140 and 180
epochs_b[:, 2, 140:180] += 0.6
```

## Tasks

::::{exercise} Build the evoked-response analysis
:label: epochs-evoked-challenge
1. Write down the meaning of every dimension.
2. Compute an evoked array for each condition.
3. Confirm the resulting shapes.
4. Extract channel 2.
5. Plot both conditions across time.
6. Plot their difference.
7. Find the time sample with the largest absolute difference.
8. Wrap the evoked calculation in a function.

Use the Python workspace below. The data generation, evoked function, shape checks,
and first plot are already in place. Run it once, inspect the output, and then extend
the code at the `TODO` comments.

<div class="live-python live-python--large">
  <textarea aria-label="Editable evoked-response analysis">import numpy as np
import matplotlib.pyplot as plt

&#35; Generate reproducible example data
rng = np.random.default_rng(7)
n_trials, n_channels, n_times = 60, 8, 300
epochs_a = rng.normal(0, 1, size=(n_trials, n_channels, n_times))
epochs_b = rng.normal(0, 1, size=(n_trials, n_channels, n_times))
epochs_b[:, 2, 140:180] += 0.6

&#35; trials × channels × time
print(&quot;epochs:&quot;, epochs_a.shape)

def compute_evoked(epochs):
    &quot;&quot;&quot;Average trials, leaving channels × time.&quot;&quot;&quot;
    return epochs.mean(axis=0)

evoked_a = compute_evoked(epochs_a)
evoked_b = compute_evoked(epochs_b)
print(&quot;evoked:&quot;, evoked_a.shape)

channel = 2
signal_a = evoked_a[channel]
signal_b = evoked_b[channel]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(signal_a, label=&quot;Condition A&quot;)
ax.plot(signal_b, label=&quot;Condition B&quot;)
ax.set(xlabel=&quot;Time sample&quot;, ylabel=&quot;Amplitude (a.u.)&quot;)
ax.legend()

&#35; TODO: calculate signal_b - signal_a
&#35; TODO: find the sample with the largest absolute difference
&#35; TODO: add the difference to this figure or create a second figure
&#35; TODO: print the peak sample

fig.tight_layout()
fig.savefig(&quot;/tmp/live_plot.png&quot;, dpi=140, bbox_inches=&quot;tight&quot;)</textarea>
  <button type="button" data-idle-label="Run analysis">Run analysis</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>
::::

::::{admonition} Hint
:class: dropdown
The first axis contains trials. Start with `epochs_a.mean(axis=0)` and inspect its
shape before plotting. `np.abs(...).argmax()` can locate the largest difference.
::::

## Reflection

::::{exercise} Scientific reflection
:label: epochs-evoked-reflection
- Which axis did you average, and what did that mean scientifically?
- Which bugs would still produce a plausible-looking figure?
- What metadata would a real analysis need to preserve?
- How would the shapes change with participants added as another dimension?
::::

::::{admonition} Hint
:class: dropdown
Separate what the array shape can verify from what requires metadata. A smooth line is
possible even when the wrong channel, time interval, or condition is selected.
::::

::::{solution} epochs-evoked-challenge
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate the same reproducible data used in the exercise
rng = np.random.default_rng(7)
n_trials, n_channels, n_times = 60, 8, 300

epochs_a = rng.normal(0, 1, size=(n_trials, n_channels, n_times))
epochs_b = rng.normal(0, 1, size=(n_trials, n_channels, n_times))
epochs_b[:, 2, 140:180] += 0.6


def compute_evoked(epochs):
    """Average trials, leaving channels × time."""
    if epochs.ndim != 3:
        raise ValueError("Expected trials × channels × time")
    return epochs.mean(axis=0)


evoked_a = compute_evoked(epochs_a)
evoked_b = compute_evoked(epochs_b)

print("epochs:", epochs_a.shape)   # trials × channels × time
print("evoked:", evoked_a.shape)  # channels × time

channel = 2
signal_a = evoked_a[channel]
signal_b = evoked_b[channel]
difference = signal_b - signal_a
peak_sample = np.abs(difference).argmax()

print("channel:", signal_a.shape)  # time
print("Peak sample:", peak_sample)

fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

axes[0].plot(signal_a, label="Condition A")
axes[0].plot(signal_b, label="Condition B")
axes[0].set(
    title="Evoked response at channel 2",
    ylabel="Amplitude (a.u.)",
)
axes[0].legend()

axes[1].plot(difference, color="black", label="B − A")
axes[1].axvline(peak_sample, color="tab:orange", linestyle="--", label="Peak")
axes[1].set(
    title="Condition difference",
    xlabel="Time sample",
    ylabel="Amplitude difference (a.u.)",
)
axes[1].legend()

fig.tight_layout()
fig.savefig("/tmp/live_plot.png", dpi=140, bbox_inches="tight")
```

`epochs_a` has shape `trials × channels × time`. Averaging `axis=0` removes the
trial dimension, so each evoked response has shape `channels × time`. Selecting
channel 2 leaves one value per time sample. The peak is defined here as the sample
where the absolute difference between conditions is largest.
::::

::::{solution} epochs-evoked-reflection
A strong explanation distinguishes code behaviour from scientific meaning. Averaging axis 0 removes individual trials and produces a channel × time evoked response. A wrong channel or time axis can still produce a smooth, plausible plot, so shape checks alone should be paired with dimension labels, units, condition metadata, sampling rate, channel names, and provenance.

Adding participants at the front would produce `participants × trials × channels × time`. Averaging trials with `axis=1` would leave `participants × channels × time`; a subsequent group mean over `axis=0` would leave `channels × time`.
::::
