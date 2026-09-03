# pandas and behavioural data

This chapter shows how to move from individual trial rows to summaries that answer a
research question. Each step has a purpose: inspect the table, check its columns,
filter invalid observations, create useful variables, and summarise by participant or
condition. Run the companion notebook alongside the examples so you can compare each
intermediate table with your own output.

```{admonition} Use this notebook
:class: important
Use **Notebook 1: Lexical decision data** for this chapter:
{doc}`open it in the book <../notebooks/01_lexical_decision_pandas>` or
{download}`download the notebook <../notebooks/01_lexical_decision_pandas.ipynb>`.
```

The small example file is available as {download}`sample trial data <../data/trials.csv>`.

```python
from pathlib import Path
import pandas as pd

trials_path = Path("book/data/trials.csv")  # locate the CSV file
trials = pd.read_csv(trials_path)            # load rows into a DataFrame
```

## Inspect before transforming

```python
trials.head()          # preview the first rows
trials.shape           # number of rows and columns
trials.columns         # available column labels
trials.dtypes          # type stored in each column
trials.isna().sum()    # count missing values by column
```

## Select and filter

```python
reaction_times = trials["reaction_time"]              # select one Series
features = trials[["reaction_time", "correct"]]      # select two columns

correct_trials = trials.loc[trials["correct"]]        # keep correct trials
condition_a = trials.query("condition == 'A'")        # keep condition A
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
    .groupby(["participant", "condition"], as_index=False)  # define the unit
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
trials["reaction_time"].isna()                         # Boolean missingness mask
trials.dropna(subset=["reaction_time"])                # remove missing rows
trials["reaction_time"].fillna(                         # replace with a summary value
    trials["reaction_time"].median()
)
```

Do not impute automatically. First ask why the value is missing.

## Merge metadata

```python
participants = pd.read_csv("book/data/participants.csv")  # participant metadata
analysis = participant_summary.merge(
    participants,
    on="participant",                  # matching key in both tables
    validate="many_to_one",             # each participant has one metadata row
)
```

`validate` turns an assumption about the relationship into a check.

## Exercise: Comment the analysis

This exercise is about **reading and explaining code**, not writing a new analysis.
Work with one or two other people. {download}`Download the complete Python script
<../workshop_scripts/comment_pandas.py>`, open it in VS Code, and run it once without
changing anything. It should print a summary table and display a figure.

The script contains a complete working analysis but almost no comments:

```{literalinclude} ../workshop_scripts/comment_pandas.py
:language: python
:linenos:
```

::::{exercise} Add comments for a future collaborator
:label: pandas-comment-code
Imagine that a new student will use this script next semester. Add comments directly
to the downloaded `.py` file that help them understand the analysis without merely
translating Python into English. Do not change the working code.

Your comments should explain:

1. where the input file is located and what one input row represents;
2. which observations are removed;
3. why reaction time is multiplied by 1,000;
4. what `.groupby(["participant", "condition"])` makes one output row represent;
5. what each new summary column contains; and
6. why sorting changes the presentation but not the calculated values;
7. why the data are summarised a second time for the plot; and
8. what the bars and error bars represent.

Add a comment above each main step and short end-of-line comments only where they make
a particular operation clearer. Do not comment every line. Run the script again to
confirm that adding comments has not changed its behaviour. When your group is done,
exchange scripts with another group: can they explain the analysis using only your
comments, the printed result, and the figure?
::::

::::{admonition} Before you run it
:class: tip
Predict the columns in `participant_summary` and whether it will have more or fewer
rows than `trials`. Record the prediction before checking it with Python.
::::

::::{solution} pandas-comment-code
There is no single correct wording. One useful version is:

```python
# Build a path that works when the project is stored in a different location.
project_dir = Path(__file__).resolve().parent.parent
trials_path = project_dir / "data" / "trials.csv"

# Load trial-level data: each row represents one experimental trial.
trials = pd.read_csv(trials_path)

# Retain correct trials with a recorded reaction time, then convert seconds to ms.
correct_trials = (
    trials
    .dropna(subset=["reaction_time"])
    .loc[lambda data: data["correct"]]
    .assign(reaction_time_ms=lambda data: data["reaction_time"] * 1000)
)

# Produce one row for every observed participant–condition combination.
participant_summary = (
    correct_trials
    .groupby(["participant", "condition"], as_index=False)
    .agg(
        mean_rt_ms=("reaction_time_ms", "mean"),  # mean correct-trial RT
        n_trials=("trial", "count"),               # retained trial count
    )
    # Arrange rows consistently without changing the summary calculations.
    .sort_values(["participant", "condition"])
)

# Average participant-level values so each participant contributes equally to a bar.
condition_summary = (
    participant_summary
    .groupby("condition", as_index=False)
    .agg(
        mean_rt_ms=("mean_rt_ms", "mean"),
        variability=("mean_rt_ms", "std"),  # between-participant standard deviation
    )
)

# Plot the condition means; error bars show between-participant variability.
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(
    condition_summary["condition"],
    condition_summary["mean_rt_ms"],
    yerr=condition_summary["variability"],
    capsize=5,
)
```

Good comments communicate the **unit of observation**, the reason for a
transformation, and the meaning of the output. A comment such as
`# use groupby` repeats the code but does not provide that information.
::::

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
