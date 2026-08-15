# Python for Cognitive Science

```{admonition} Two Python days. One shared foundation.
:class: tip
Refresh the Python you already know and make it reliable enough for cognitive neuroscience, natural language processing, and data science.
```

This is an interactive workshop for incoming MSc Cognitive Science students at Aarhus University. The first two days revisit Python for three courses on the programme:

- **Advanced Cognitive Neuroscience**
- **Natural Language Processing**
- **Data Science, Prediction and Forecasting**

The courses use Python for different scientific purposes, but they rely on the same fundamentals: values and types, collections, control flow, functions, objects, files, arrays, tables, visualisation, and reproducible environments. This workshop revisits that shared foundation before connecting it to course-specific examples.

**Day 3 is being developed separately and will focus on responsible use of generative AI.** It will have its own notebook; details will be added when the programme is ready.

It is not designed as a first introduction to programming. The aim is to make familiar ideas available again, fill in gaps, and build dependable habits for reading and debugging research code. See {doc}`course_overview` for a map of what each course is likely to require.

## What you will be able to do

By the end of the workshop, you can:

- create a reproducible Python environment in VS Code;
- navigate research projects safely with `pathlib`;
- understand objects, methods, attributes, and dictionaries;
- reason about NumPy shapes, dimensions, and axes;
- turn 3D epochs into an evoked response;
- make clear figures with Matplotlib;
- clean and summarise experimental data with pandas;
- recognise the shared `fit`/`predict` workflow of data-science models;
- work effectively with the data structures used in NLP;
- diagnose common errors before asking for help.

## How the workshop works

Each block follows the same rhythm:

1. **Predict** before running the code.
2. **Discuss** plausible answers anonymously.
3. **Run** and inspect the result.
4. **Explain** what Python did and why.
5. **Vary** the example independently.

The CodeQuiz extension lets everyone answer inside a Python script. Responses are anonymous, and the instructor controls when solutions appear.

CodeQuiz and the notebooks do different jobs. A quiz is a short, shared checkpoint: everyone commits to a prediction, the class sees the distribution of answers, and the instructor can decide whether to move on or revisit an idea. A notebook is the longer individual investigation that follows, where you write, run, debug, and vary the code. Quiz answers are anonymous classroom data; notebook work remains yours.

```{figure} _static/cartoons/xkcd-python.png
:alt: Two people discuss how learning Python apparently lets one of them fly by importing antigravity.
:width: 420px
:align: center

Python can feel a little like this, although most workshop exercises obey gravity. [“Python” by Randall Munroe](https://xkcd.com/353/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

```{admonition} The workshop principle
Knowing syntax is not the same as having a dependable mental model. We care about what your objects contain, which dimensions your arrays have, and what each transformation means scientifically.
```

## Course connections

| Workshop foundation | ACN | NLP | Data Science |
|---|---:|---:|---:|
| Paths and environments | ✓ | ✓ | ✓ |
| Objects, methods, attributes | ✓ | ✓ | ✓ |
| Dictionaries and comprehensions | ✓ | ✓ | ✓ |
| NumPy shapes and axes | ✓ | ✓ | ✓ |
| Matplotlib | ✓ | ✓ | ✓ |
| pandas | useful | ✓ | ✓ |
| Model API and feature matrices | useful | ✓ | ✓ |

Start with {doc}`setup`, then keep {doc}`resources/cheatsheet` open during the exercises.

## A note on Python documentation

This book contains explanations and worked examples, but no workshop can document every library function. An important learning goal is therefore knowing how to investigate an unfamiliar object. The chapter {doc}`foundations/reading_documentation` shows how to use `help()`, docstrings, signatures, official API references, and small experiments.
