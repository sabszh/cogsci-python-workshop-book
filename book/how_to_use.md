# How to use this book

This book is a workshop companion, not a textbook to read from beginning to end.

It serves three purposes:

- a guided path through the two workshop days;
- a place to predict, practise, and inspect examples;
- a reference you can return to during ACN, NLP, and Data Science.

If a chapter is familiar, begin with its exercises. If your prediction is wrong or uncertain, return to the explanation and recreate the example with smaller values.

## During demonstrations

- Keep the relevant page open.
- Type code yourself instead of copying large blocks.
- Predict values and shapes before execution.
- Add temporary `print`, `type`, and `.shape` checks.
- Keep your first answer when the solution is revealed; compare them.

## Notebook work

The notebooks are the main place to practise. Each notebook moves from a small
prediction to runnable code, inspection, and an independent variation. Work through the
examples in order when you are learning a concept; return to a particular exercise later
when you need a refresher.

Use this map whenever a chapter asks you to open a notebook:

| Notebook | Use it for |
|---|---|
| **Notebook 0: Python warm-up** | Python foundations and objects |
| **Notebook 1: Lexical decision data** | pandas and behavioural data |
| **Notebook 2: EEG arrays** | NumPy dimensions, EEG, and visualisation |
| **Notebook 3: Model workflow** | features, targets, fitting, and evaluation |
| **Notebook 4: NLP text features** | text preprocessing and representations |

Open or download them from the {doc}`notebook overview <notebooks>`.

A typical cycle is:

1. Read the prompt and predict the output, type, shape, or likely bug.
2. Write or edit the smallest piece of code that tests the idea.
3. Run the cell and inspect the result.
4. Compare the result with your prediction.
5. Change one input or condition and run it again.

The aim is not to finish as quickly as possible. It is to make your mental model more
reliable through small, repeatable experiments.

## Exercise labels

::::{exercise} Predict
:label: example-predict
What does `list(range(2, 8, 2))` produce?
::::

::::{admonition} Hint
:class: dropdown
`range(start, stop, step)` includes `start`, advances by `step`, and excludes `stop`.
::::

::::{solution} example-predict
`[2, 4, 6]`. The stop value `8` is excluded.
```

```{admonition} Course connection
:class: note
These callouts explain where a technique appears in ACN, NLP, or Data Science.
```

```{admonition} Debugging habit
:class: tip
These callouts suggest a small, repeatable diagnostic action.
::::

## Productive struggle

Richard McElreath writes, “It is important that readers expect that confusion is
normal” in the preface to [*Statistical Rethinking*](https://www.yfish.org/assets/pdf/McElreath_2020_Statistical_Rethinking.pdf).
When something is unclear, write down four facts: the object's type, its shape or
length, the result you expected, and the result Python produced. That usually turns a
vague problem into a specific question.

Spend a few minutes investigating before viewing a solution:

1. Read the final line of the traceback.
2. Inspect the relevant object's `type`.
3. Inspect array or DataFrame shapes.
4. Reduce the problem to the smallest failing example.
5. Explain what you expected and what happened instead.

## Your private answers

Most exercises include a **Your answer** field. Write your prediction before opening the solution, then leave the field visible while you compare the two. The visualisation challenges use an editable Python plot instead, so you can make and test your changes directly in the page.

Your answer is saved automatically in this browser using local storage. It is not submitted to the instructor or uploaded to the workshop site. Notes do not automatically follow you to another browser, device, or private-browsing session, and clearing browser site data removes them. Use **Clear note** to remove an individual answer.

## How to study an example

For every non-trivial code block, annotate it with four questions:

1. What are the input objects and their types?
2. Which operation is performed?
3. What type and structure does the operation return?
4. What does the result mean scientifically?

For arrays and tables, add a fifth: **what does each dimension, row, or column represent?**

## Code is meant to be changed

Do not only run the provided examples. Change one feature at a time:

- replace a value;
- add an item to a collection;
- choose another axis;
- introduce a missing value;
- rename a column;
- remove a pair of parentheses;
- inspect the resulting error or changed output.

Small controlled changes help distinguish what Python guarantees from what happened accidentally in one example.
