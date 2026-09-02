# Integrated Cognitive Science challenge

This challenge brings together the workshop's shared foundations in one small research
analysis. Work together to make the data, transformations, and results understandable.

Open `book/workshop_scripts/capstone_starter.py` directly from the cloned repository,
or {download}`download a separate copy <../workshop_scripts/capstone_starter.py>`.

```{admonition} Files for this challenge
:class: important
The main file is **`capstone_starter.py`** above. This challenge also brings together
**Notebook 1: Lexical decision data**, **Notebook 2: EEG arrays**, **Notebook 3: Model
workflow**, and **Notebook 4: NLP text features**. Find every notebook on the
{doc}`notebook overview <../notebooks>`.
```

## Scenario

You are analysing a small experiment containing:

- participant metadata;
- trial-level reaction times and accuracy;
- two conditions of simulated neural epochs;
- short free-text participant responses.

## Deliverables

### 1. Project and data

- Locate data with `pathlib`.
- Load participants and trials with pandas.
- Validate expected columns and relationships.

### 2. Behaviour

- Remove trials without a reaction time.
- Calculate accuracy and mean correct-trial reaction time per participant and condition.
- Visualise the condition comparison.

### 3. Neuroscience

- Simulate or load `trials × channels × time` epochs.
- Document every dimension.
- Compute evoked responses.
- Plot one channel and the condition difference.

### 4. Data Science

- Construct a participant-level feature matrix.
- Define a target.
- Split data reproducibly.
- Fit a simple pipeline and evaluate it.
- Explain why the result is only illustrative with such a small dataset.

### 5. NLP

- Store responses as dictionaries.
- Extract text and labels.
- Convert text into a small feature matrix.
- Report the resulting shape and feature names.

## Required checks

Your script should contain assertions such as:

```python
assert epochs.ndim == 3
assert evoked.shape == epochs.shape[1:]
assert X.shape[0] == len(y)
assert participant_summary["participant"].notna().all()
```

## Explain one result to your group

::::{exercise} Connect the code to the scientific result
:label: capstone-explanation
Choose **one result your group produced**: the behavioural condition difference, the
evoked-response difference, the model predictions, or the text-feature matrix. Write
five short statements:

1. What data went into this step? Include its unit of observation and shape.
2. What was calculated or selected?
3. What came out? Include its shape.
4. What does the result mean for this small experiment?
5. What can you **not** conclude from it?

Do not describe only the Python syntax. Someone who has not seen the script should be
able to understand what information was retained and what was discarded.
::::

::::{admonition} Hint
:class: dropdown
For the neural result, begin with: “Each condition contained 60 trials × 8 channels ×
300 time samples.” Then state which dimension disappeared and why. For behaviour,
identify whether each output row represents a trial, participant, or condition.
::::

::::{solution} capstone-explanation
A complete neural-response explanation could read:

> Each condition contained 60 trials × 8 channels × 300 time samples. We averaged the
> 60 trials within each condition, producing an 8 × 300 channel-by-time array. The
> resulting curves describe the mean simulated response in each condition; individual
> trial variation is no longer visible. Their difference does not establish that a
> condition caused a neural effect because the data are simulated and no uncertainty
> estimate or participant sample is included.

Another result needs different nouns and limitations, but should answer the same five
questions.
::::

```{figure} ../_static/cartoons/xkcd-correlation.png
:alt: A person says a statistics class changed their belief that correlation implies causation, accidentally making another causal claim.
:width: 520px
:align: center

Keep this distinction in the final sentence of your explanation. [“Correlation” by Randall Munroe](https://xkcd.com/552/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```
