# Day 1 challenge · Epochs to evoked

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
evoked_a = epochs_a.mean(axis=0)
evoked_b = epochs_b.mean(axis=0)
difference = evoked_b - evoked_a

channel = 2
peak_sample = np.abs(difference[channel]).argmax()

print(evoked_a.shape)
print("Peak sample:", peak_sample)
```
::::

::::{solution} epochs-evoked-reflection
A strong explanation distinguishes code behaviour from scientific meaning. Averaging axis 0 removes individual trials and produces a channel × time evoked response. A wrong channel or time axis can still produce a smooth, plausible plot, so shape checks alone should be paired with dimension labels, units, condition metadata, sampling rate, channel names, and provenance.

Adding participants at the front would produce `participants × trials × channels × time`. Averaging trials with `axis=1` would leave `participants × channels × time`; a subsequent group mean over `axis=0` would leave `channels × time`.
::::
