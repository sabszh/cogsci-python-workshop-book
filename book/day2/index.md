# Overview and warm-up

Day 2 uses yesterday's object and array reasoning to organise behavioural data, write
analysis functions, and prepare inputs for models.

```{admonition} Today's notebooks
:class: important
- **Notebook 1: Lexical decision data** — {doc}`open <../notebooks/01_lexical_decision_pandas>` or {download}`download <../notebooks/01_lexical_decision_pandas.ipynb>`
- **Notebook 3: Model workflow** — {doc}`open <../notebooks/03_model_workflow>` or {download}`download <../notebooks/03_model_workflow.ipynb>`
- **Notebook 4: NLP text features** — {doc}`open <../notebooks/04_nlp_text_features>` or {download}`download <../notebooks/04_nlp_text_features.ipynb>`
```

## Retrieval warm-up

::::{exercise} Retrieve yesterday's axis reasoning
:label: day2-retrieval
For an array shaped `participants × trials × channels × time`:

1. Which axis produces a participant-level average across trials?
2. What shape remains?
3. Which expression extracts channel 4 for all participants, trials, and times?
::::

::::{admonition} Hint
:class: dropdown
An aggregation removes the axis it operates on. A colon retains every value along an
axis; an integer selects one position and removes that axis.
::::

::::{solution} day2-retrieval
1. `axis=1`
2. `participants × channels × time`
3. `data[:, :, 4, :]`
::::

## Today's pipeline

```text
files
  → DataFrame / arrays
  → validation
  → clean transformations
  → participant-level summaries
  → feature matrix X and target y
  → model
  → evaluation
```

You will not learn every model in one workshop. The useful common ground is the Python
structure underneath regression, classification, NLP, and cognitive modelling.
