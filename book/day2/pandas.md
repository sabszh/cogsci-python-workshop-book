# pandas and behavioural data

This chapter shows how to move from individual trial rows to summaries that answer a
research question. Each step has a purpose: inspect the table, check its columns,
filter invalid observations, create useful variables, and summarise by participant or
condition. Run the linked notebook alongside the examples so you can compare each
intermediate table with your own output.

This chapter introduces the pandas operations used with trial-level behavioural data.
The corresponding Day 2 notebook is listed in the {doc}`../notebooks` section; there is
no need to leave this chapter while following the examples below.

The small example file is available as {download}`sample trial data <../data/trials.csv>`.

```python
from pathlib import Path
import pandas as pd

trials_path = Path("book/data/trials.csv")
trials = pd.read_csv(trials_path)
```

## Inspect before transforming

```python
trials.head()
trials.shape
trials.columns
trials.dtypes
trials.isna().sum()
```

## Select and filter

```python
reaction_times = trials["reaction_time"]
features = trials[["reaction_time", "correct"]]

correct_trials = trials.loc[trials["correct"]]
condition_a = trials.query("condition == 'A'")
```

<div class="live-python">
  <p><strong>Check with Python:</strong> change the filter or grouped column and inspect the table.</p>
  <textarea aria-label="Editable pandas filtering and grouping example">import pandas as pd
trials = pd.DataFrame({
    &quot;participant&quot;: [&quot;P01&quot;, &quot;P01&quot;, &quot;P02&quot;, &quot;P02&quot;],
    &quot;condition&quot;: [&quot;A&quot;, &quot;B&quot;, &quot;A&quot;, &quot;B&quot;],
    &quot;reaction_time&quot;: [0.51, 0.73, 0.62, 0.81],
    &quot;correct&quot;: [True, True, False, True],
})
correct = trials.loc[trials[&quot;correct&quot;]]
summary = correct.groupby(&quot;condition&quot;)[&quot;reaction_time&quot;].mean()
print(summary)</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Group at the correct unit of analysis

```{admonition} Common mistake
:class: dropdown warning
After `groupby()`, one row may represent a participant or condition rather than a
trial. State the unit of one row before merging the result or fitting a model.
```

```python
participant_summary = (
    trials
    .groupby(["participant", "condition"], as_index=False)
    .agg(
        mean_rt=("reaction_time", "mean"),
        accuracy=("correct", "mean"),
        n_trials=("trial", "count"),
    )
)
```

```{admonition} Scientific question first
:class: warning
Averaging every trial together weights participants with more retained trials more heavily. Decide whether the inferential unit is a trial or participant before aggregating.
```

## Missing values

```python
trials["reaction_time"].isna()
trials.dropna(subset=["reaction_time"])
trials["reaction_time"].fillna(trials["reaction_time"].median())
```

Do not impute automatically. First ask why the value is missing.

## Merge metadata

```python
participants = pd.read_csv("book/data/participants.csv")
analysis = participant_summary.merge(
    participants,
    on="participant",
    validate="many_to_one",
)
```

`validate` turns an assumption about the relationship into a check.

::::{exercise} Participant summaries
:label: pandas-summary
For correct trials only, calculate each participant's mean reaction time in each condition. Sort from fastest to slowest.
::::

::::{admonition} Hint
:class: dropdown
Filter rows first, group by both `participant` and `condition`, aggregate
`reaction_time`, then sort the resulting column.
::::

::::{solution} pandas-summary
```python
result = (
    trials
    .loc[trials["correct"]]
    .groupby(["participant", "condition"], as_index=False)
    .agg(mean_rt=("reaction_time", "mean"))
    .sort_values("mean_rt")
)
```
::::
