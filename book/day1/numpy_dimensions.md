# NumPy dimensions and axes

This is the central technical idea of Day 1.

The {doc}`../notebooks/02_real_eeg_arrays` notebook applies indexing, Boolean masks, aggregation, and reshaping to a real EEG recording.

## Start with meaning, then shape

We represent epochs as:

```text
trials × channels × time
```

```python
import numpy as np

rng = np.random.default_rng(42)
epochs = rng.normal(size=(80, 32, 500))

print(epochs.shape)  # (80, 32, 500)
print(epochs.ndim)   # 3
```

| Axis | Meaning | Size |
|---:|---|---:|
| 0 | trials | 80 |
| 1 | channels | 32 |
| 2 | time samples | 500 |

<div class="axis-explorer">
  <p><strong>Axis explorer</strong></p>
  <p>Start with <code>(80, 32, 500)</code>, meaning trials × channels × time.</p>
  <label>Average over
    <select aria-label="Axis to average">
      <option value="0">axis 0: trials</option>
      <option value="1">axis 1: channels</option>
      <option value="2">axis 2: time samples</option>
    </select>
  </label>
  <output aria-live="polite"></output>
</div>

<div class="live-python">
  <p><strong>Check with Python:</strong> change <code>axis</code> and compare the printed shape with the explorer.</p>
  <textarea aria-label="Editable NumPy axis example">import numpy as np
epochs = np.zeros((80, 32, 500))
axis = 0
evoked = epochs.mean(axis=axis)
print(&quot;input:&quot;, epochs.shape)
print(&quot;output:&quot;, evoked.shape)</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Indexing removes selected dimensions

```python
epochs[0].shape          # one trial → (32, 500)
epochs[:, 0, :].shape    # one channel, all trials → (80, 500)
epochs[:, :, 100].shape  # one time point → (80, 32)
epochs[0, 0, 100]        # one scalar
```

<div class="live-python">
  <p><strong>Check with Python:</strong> change the indexing expression on the final line.</p>
  <textarea aria-label="Editable NumPy indexing example">import numpy as np
epochs = np.zeros((80, 32, 500))
selection = epochs[:, 0, :]
print(selection.shape)</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Aggregation removes an axis

```{admonition} Common mistake
:class: dropdown warning
The number passed to `axis` identifies the dimension being removed, not the dimension
you want to keep. Write the meaning above every dimension before calculating a mean.
```

```python
evoked = epochs.mean(axis=0)
print(evoked.shape)  # (32, 500)
```

We averaged trials, so the trial dimension disappeared. This is not merely a Python operation; it is a scientific decision about which observations to combine.

::::{exercise} Predict the shapes
:label: numpy-shapes
For `epochs.shape == (80, 32, 500)`, predict:

1. `epochs.mean(axis=1).shape`
2. `epochs.mean(axis=2).shape`
3. `epochs.mean(axis=(0, 1)).shape`
4. `epochs.mean(axis=0, keepdims=True).shape`
::::

::::{admonition} Hint
:class: dropdown
Indexing with an integer removes that selected axis. Calling `.mean(axis=n)` removes
axis `n`; all other axes remain in the same order.
::::

::::{solution} numpy-shapes
1. `(80, 500)`: channels removed.
2. `(80, 32)`: time removed.
3. `(500,)`: trials and channels removed.
4. `(1, 32, 500)`: trial axis retained with size one.
::::

## Broadcasting

Subtract a baseline for every trial and channel:

```python
baseline = epochs[:, :, :100].mean(axis=2, keepdims=True)
corrected = epochs - baseline

print(baseline.shape)   # (80, 32, 1)
print(corrected.shape)  # (80, 32, 500)
```

NumPy stretches the final size-one dimension across time.

<div class="live-python">
  <p><strong>Check with Python:</strong> remove <code>keepdims=True</code> and inspect why subtraction then fails.</p>
  <textarea aria-label="Editable NumPy broadcasting example">import numpy as np
epochs = np.ones((4, 3, 10))
baseline = epochs[:, :, :2].mean(axis=2, keepdims=True)
corrected = epochs - baseline
print(&quot;epochs:&quot;, epochs.shape)
print(&quot;baseline:&quot;, baseline.shape)
print(&quot;corrected:&quot;, corrected.shape)</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Shape-first debugging

Before a transformation, write:

```python
print("epochs:", epochs.shape)
print("baseline:", baseline.shape)
```

If you cannot describe what every dimension means, pause before continuing.

```{admonition} Transfer
:class: note
The same reasoning applies to NLP tensors such as `batch × tokens × embedding dimensions` and data-science matrices such as `samples × features`.
```
