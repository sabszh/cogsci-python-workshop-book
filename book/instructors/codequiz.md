# CodeQuiz prompt bank

These prompts are designed for the annotated Python script format used by the extension.

## Day 1

1. List aliasing after `.append()`
2. Nested dictionary shallow copy
3. Attribute versus method: `path.exists` and `path.exists()`
4. Relative path resolution
5. Shape after selecting one channel
6. Shape after `mean(axis=0)`
7. Shape after `mean(axis=(0, 2))`
8. Broadcasting with a `(trials, channels, 1)` baseline
9. Matplotlib x/y dimension mismatch
10. Line or bar chart for unordered experimental conditions
11. What information an error bar does and does not contain
12. Choose the most informative title for a result figure

## Day 2

1. Function with no explicit `return`
2. Mutation inside a function
3. DataFrame row/column selection
4. `groupby` output granularity
5. Missing reaction-time handling
6. `X` and `y` shapes
7. Scaling before versus inside a pipeline
8. NLP tensor aggregation
9. Method versus learned attribute: `.fit()` and `.coef_`

## Repeat items

Repeat structurally equivalent questions across the two days:

```text
trials × channels × time
documents × tokens × embeddings
samples × features
```

The surface changes while the dimensional reasoning stays the same.

Open `book/workshop_scripts/live_codequiz.py` in the cloned repository, or
{download}`download a separate copy <../workshop_scripts/live_codequiz.py>`.
