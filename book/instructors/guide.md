# Instructor guide

## Teaching principles

- Ask for a prediction before executing code.
- Collect answers anonymously.
- Discuss plausible wrong answers, not only the correct answer.
- Alternate worked examples with faded guidance.
- Revisit concepts across contexts: array axes in ACN, feature matrices, and NLP tensors.
- Avoid turning the workshop into a syntax marathon.

## Before the workshop

- Ask students to complete the setup diagnostic.
- Test CodeQuiz on the actual classroom network.
- Keep a local-network and non-CodeQuiz fallback.
- Print or distribute the cheatsheet.
- Review entry-test results without identifying students.

## Live rhythm

| Minutes | Activity |
|---:|---|
| 5 | Retrieval question |
| 10 | Concise explanation |
| 10 | Worked example |
| 20 | Guided practice |
| 10 | Independent variation |
| 5 | CodeQuiz and synthesis |

## What CodeQuiz adds

CodeQuiz is most useful at decision points, not as a second worksheet. Use it to:

- make every student predict before the fastest voice answers;
- distinguish a widespread misconception from one isolated question;
- compare the reasoning behind different answers;
- choose whether to explain, demonstrate, or let students continue;
- repeat the same concept in a new surface form later in the day.

Useful prompt types include **predict the output**, **fill one blank**, **which axis?**, **spot the bug**, and **choose the inspection that would settle the question**. Keep most prompts small enough to reason about without executing them.

After submissions, show the answer distribution first. Ask someone to defend each plausible answer without identifying who submitted it. Reveal the result only after the competing mental models are clear, then let students verify it in Python.

Do not use CodeQuiz for long implementations. Once a task needs several transformations or debugging attempts, move into the notebook. The quiz provides a class-level signal; the notebook provides practice.

## When answers are wrong

Ask:

- What assumption makes this answer reasonable?
- Which object or axis did we interpret differently?
- What single inspection would distinguish the alternatives?
- Could this bug produce a plausible scientific result?

## Privacy

- Keep submissions anonymous.
- Display grouped answers, not participant histories.
- Do not grade the diagnostic or retrieval checks.
- Report class-level change only.
- Do not infer individual performance from repeated anonymous answers.

## Pacing decisions

If time is short, protect NumPy shapes/axes, `pathlib`, environments, functions, and pandas grouping. Shorten the model and NLP demonstrations rather than rushing the foundations.
