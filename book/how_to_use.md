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

## CodeQuiz and notebooks

The two activities have different tempos:

| CodeQuiz | Notebook |
|---|---|
| one focused question | a connected analysis |
| answer before running | experiment by running code |
| anonymous class response | individual work |
| reveals patterns across the room | reveals the steps in your own reasoning |
| usually 2–5 minutes | usually 15–35 minutes |

A typical cycle is:

1. Open the quiz marker in the instructor's Python script.
2. Predict the output, missing expression, shape, or likely bug.
3. Submit anonymously in VS Code.
4. Discuss the answer distribution before revealing the solution.
5. Test the underlying idea in the notebook.
6. Return to a short quiz with a changed example.

The first quiz is not a mini-exam. Its purpose is to make everyone commit to a mental model. The second shows whether that model survived contact with the code.

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

Every exercise includes a **Your answer** field. Write your prediction before opening the solution, then leave the field visible while you compare the two.

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
