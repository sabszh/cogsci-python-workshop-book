# Overview and warm-up

Day 1 connects everyday Python concepts to multidimensional cognitive-neuroscience data.

```{admonition} Today's notebooks
:class: important
- **Notebook 0: Python warm-up** — {doc}`open <../notebooks/00_python_warmup>` or {download}`download <../notebooks/00_python_warmup.ipynb>`
- **Notebook 2: EEG arrays** — {doc}`open <../notebooks/02_eeg_arrays>` or {download}`download <../notebooks/02_eeg_arrays.ipynb>`
```

## Today's questions

- Which Python interpreter is actually running my code?
- Where should a script look for its data?
- What is the difference between an object, method, and attribute?
- Which dimensions does my array contain?
- What exactly disappears when I average over an axis?

## Retrieval warm-up

::::{exercise} Retrieval warm-up
:label: day1-retrieval
Answer before running. Write down both outputs.

```python
values = [1, 2, 3]
alias = values
alias.append(4)

print(values)
```

```python
participant = {"id": "P01", "scores": [7, 9, 8]}
participant["scores"].append(10)

print(participant["scores"][-1])
```

We will return to the same mental models throughout the day.
::::

::::{admonition} Hint
:class: dropdown
`alias = values` assigns another name to the same list. Index `-1` selects the final
item of a sequence.
::::

::::{solution} day1-retrieval
The outputs are:

```text
[1, 2, 3, 4]
10
```

`values` and `alias` refer to the same mutable list, so appending through `alias` is visible through `values`. The nested score list is also mutable; `.append(10)` adds an item, and index `-1` retrieves the final value.
::::
