# Visualisation with Matplotlib

[Matplotlib](https://matplotlib.org/stable/) is the plotting library underneath pandas
plots, seaborn, and much of MNE's visualisation. Its gallery is useful when you know
what a plot should look like but not which method makes it: find a nearby example, then
inspect its code.

The object-oriented interface is easier to extend than a chain of `plt.*` calls. `fig`
is the complete canvas; `ax` is one plotting area with methods such as `.plot()`,
`.set_xlabel()`, and `.legend()`.

```python
import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(-0.2, 0.8, 500)
evoked = epochs.mean(axis=0)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(times, evoked[0], label="channel 0")
ax.axvline(0, color="black", linestyle="--", linewidth=1)
ax.set(
    title="Evoked response",
    xlabel="Time (s)",
    ylabel="Amplitude",
)
ax.legend()
fig.tight_layout()
```

## Plot two conditions

The shaded region below marks the distance between two condition averages. It is not
an uncertainty interval unless the two arrays actually contain interval boundaries.

```python
fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(times, evoked_a[0], label="condition A")
ax.plot(times, evoked_b[0], label="condition B")
ax.fill_between(times, evoked_a[0], evoked_b[0], alpha=0.15)
ax.axvline(0, color="black", linestyle="--")
ax.legend()
```

<div class="figure-explorer">
  <p><strong>Figure explorer</strong></p>
  <label>Signal amplitude
    <input data-amplitude type="range" min="2" max="35" value="18">
  </label>
  <label>Added noise
    <input data-noise type="range" min="0" max="18" value="5">
  </label>
  <svg viewBox="0 0 620 180" role="img" aria-label="Two simulated condition traces controlled by signal amplitude and noise sliders">
    <line x1="35" y1="145" x2="585" y2="145" stroke="#333" />
    <line x1="35" y1="20" x2="35" y2="145" stroke="#333" />
    <text x="280" y="172" fill="#222">Time</text>
    <text x="12" y="90" fill="#222" transform="rotate(-90 12 90)">Amplitude</text>
    <polyline data-line-a fill="none" stroke="#4477AA" stroke-width="3" />
    <polyline data-line-b fill="none" stroke="#CC6677" stroke-width="3" stroke-dasharray="8 5" />
    <text x="470" y="30" fill="#4477AA">condition A</text>
    <text x="470" y="50" fill="#9b4050">condition B</text>
  </svg>
  <output aria-live="polite"></output>
</div>

## Plot shape must match

```{admonition} Common mistake
:class: dropdown warning
Matplotlib can only pair x and y values when their relevant dimensions agree. If a
plot fails after an average, inspect the new shape before changing the plotting code.
```

For `ax.plot(x, y)`, the relevant dimensions of `x` and `y` must agree.

::::{exercise} Find the mismatch
:label: plot-mismatch
Why does this fail?

```python
times = np.linspace(-0.2, 0.8, 500)
channel_means = epochs.mean(axis=2)
ax.plot(times, channel_means[0])
```
::::

::::{admonition} Hint
:class: dropdown
Inspect `times.shape`, `channel_means.shape`, and `channel_means[0].shape`. Which
operation removed the 500-sample time dimension?
::::

::::{solution} plot-mismatch
`channel_means.shape` is `(80, 32)`, so `channel_means[0]` contains 32 channel values.
`times` contains 500 time values. Averaging `axis=2` removed time, the dimension
intended for the x-axis.
::::

## Minimum figure checklist

- Does every axis have a label and unit?
- Does the title describe the comparison rather than the plotting command?
- Can colours be distinguished without relying on red versus green?
- Is uncertainty shown when appropriate?
- Does the plotted array contain the dimension you think it does?

## Accessibility is part of the figure

Do not encode a condition by colour alone. Combine colour with a line style, marker,
direct label, or position so that the comparison also works in greyscale. Avoid a
red–green pairing: the [Matplotlib colormap guide](https://matplotlib.org/stable/users/explain/colors/colormaps.html#color-vision-deficiencies)
notes that red–green discrimination is the most common colour-vision difficulty.

For ordered numerical values, use a perceptually uniform map such as `viridis`,
`cividis`, `magma`, or `plasma`. For two experimental conditions, explicit colours plus
different markers or line styles are usually clearer than a colormap.

```python
ax.plot(times, evoked_a[0], color="#4477AA", linestyle="-", label="condition A")
ax.plot(times, evoked_b[0], color="#CC6677", linestyle="--", label="condition B")
```

Check text size, contrast, and the final export size. Save an SVG when possible for
scalable text and lines, or use a sufficiently high-resolution PNG:

```python
fig.savefig("evoked.svg", bbox_inches="tight")
fig.savefig("evoked.png", dpi=300, bbox_inches="tight")
```

A caption or nearby paragraph should state the main pattern so the interpretation is
not available only through the image.

## Challenge 1 · Repair the plot

This code runs, but it omits information needed to interpret the values.

```python
conditions = ["congruent", "incongruent", "neutral"]
mean_rt = [515, 681, 552]

fig, ax = plt.subplots()
ax.plot(conditions, mean_rt, "r*-.")
plt.show()
```

::::{exercise} Repair the plot
:label: figure-rescue
Make at least four changes. Include an informative title, a y-axis label with units,
and visual cues that do not depend only on colour. Decide whether the three points
should be connected and explain that decision.
::::

::::{admonition} Hint
:class: dropdown
Start with the y-axis label and units. Then ask whether a line between unordered
conditions implies a meaningful continuum. Direct value labels can reduce reliance on
colour.
::::

::::{solution} figure-rescue
One possible version is:

```python
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(
    conditions,
    mean_rt,
    color=["#4477AA", "#EE6677", "#BBBBBB"],
    edgecolor="black",
)
ax.set(
    title="Responses slow down on incongruent Stroop trials",
    xlabel="Trial condition",
    ylabel="Mean reaction time (ms)",
)
ax.bar_label(bars, fmt="%.0f ms", padding=3)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
```

A bar chart does not imply measured values between these nominal conditions. Direct
labels keep the numerical comparison available without colour.
::::

## Challenge 2 · Show the uncertainty

The means below come from the same fictional Stroop experiment. The second array is
the standard error of each mean.

```python
mean_rt = np.array([515, 681, 552])
sem_rt = np.array([18, 24, 20])
```

::::{exercise} Add uncertainty and an annotation
:label: uncertainty-plot
Add uncertainty to your repaired figure. Annotate the incongruent condition with the
difference from the congruent condition. Calculate the difference in Python rather
than typing `166` into the annotation.
::::

::::{admonition} Hint
:class: dropdown
`ax.errorbar(..., yerr=sem_rt, capsize=5)` adds the standard errors. Calculate the
annotation with `mean_rt[1] - mean_rt[0]`.
::::

::::{solution} uncertainty-plot
For example:

```python
difference = mean_rt[1] - mean_rt[0]

fig, ax = plt.subplots(figsize=(7, 4))
ax.errorbar(
    conditions,
    mean_rt,
    yerr=sem_rt,
    fmt="o",
    markersize=9,
    capsize=5,
    color="#332288",
)
ax.annotate(
    f"+{difference:.0f} ms",
    xy=(1, mean_rt[1]),
    xytext=(1.25, mean_rt[1] + 35),
    arrowprops={"arrowstyle": "->"},
)
ax.set(title="Stroop interference", ylabel="Mean reaction time (ms)")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
```

The caption must identify the error bars; here they are standard errors.
::::

## Challenge 3 · Figure remix

The script `book/workshop_scripts/matplotlib_challenge.py` opens directly from the
cloned repository. You can also {download}`download a separate copy <../workshop_scripts/matplotlib_challenge.py>`.
It contains reaction times from eight fictional participants in congruent, incongruent,
and neutral Stroop trials. Work in pairs and choose one question:

- How much slower is the incongruent condition for the average participant?
- Is the condition difference consistent across participants?
- Which participant departs most from the group pattern?

Your question determines whether you need condition means, paired participant lines,
or both.

::::{exercise} Build the figure around one question
:label: figure-showdown
Create and export one figure. It must:

- answer the question you selected above;
- include labels and units;
- show participant observations if your claim concerns consistency between people;
- distinguish conditions without depending on colour alone;
- annotate the numerical comparison mentioned in your title or caption.

Save the result as `stroop_remix.png`. We will compare how different plotting choices
answer different questions from the same array.
::::

::::{admonition} Hint
:class: dropdown
`participant_rt` has shape `participants × conditions`. Loop over its rows to draw one
line per participant. Use `mean_rt` and `sem_rt` for the group summary. If the legend
becomes crowded, label only the conditions and explain the grey lines in the caption.
::::

::::{solution} figure-showdown
There is no single required geometry, but the saved figure should pass these checks:

```python
assert ax.get_title()
assert ax.get_xlabel()
assert "ms" in ax.get_ylabel().lower()
fig.savefig("stroop_remix.png", dpi=160, bbox_inches="tight")
```

A suitable caption might be: “Thin lines show individual participants; points and
error bars show condition means ± SEM. All eight participants responded more slowly
on incongruent than congruent trials.” The example at the bottom of the starter script
can be opened after the comparison.
::::

## Matplotlib references

- [Quick-start guide](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Examples gallery](https://matplotlib.org/stable/gallery/index.html)
- [Choosing colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html)
- [Accessible colour and text guidance for scientific plots](https://www.sandia.gov/fairer-data/equitable-accessibility/)
