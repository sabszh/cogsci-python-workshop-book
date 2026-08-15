# Python across the MSc courses

Python is a shared research tool across the programme rather than a topic that belongs to only one course. The same language constructs reappear in different scientific settings.

This workshop primarily prepares you for three courses:

- **Advanced Cognitive Neuroscience (ACN)**, where Python supports loading, organising, transforming, averaging, and visualising multidimensional neuroscience data.
- **Natural Language Processing (NLP)**, where Python is used to represent text, build processing pipelines, create numeric features, and interact with machine-learning models.
- **Data Science, Prediction and Forecasting**, where Python supports tabular data analysis, statistical learning, model evaluation, and reproducible prediction workflows.

```{admonition} Scope of this workshop
:class: note
We focus on transferable Python fundamentals. We will not try to teach the complete neuroscience, NLP, or statistical-learning curriculum in two days.
```

## What is shared?

All three courses require you to move between three levels of understanding:

1. **Python level:** What does this expression do?
2. **data level:** What type, shape, columns, or keys does the object have?
3. **scientific level:** What does this transformation mean for the research question?

For example:

```python
result = data.mean(axis=0)
```

At the Python level, this calls a method. At the data level, it removes an axis by averaging. At the scientific level, its meaning depends on whether axis 0 represents participants, trials, documents, or something else.

## Advanced Cognitive Neuroscience

Typical tasks include handling participant files, understanding library objects, working with epochs, averaging signals, and plotting results.

| Foundation | Why it matters in ACN |
|---|---|
| `pathlib` and file patterns | Locate participant, condition, and recording files safely |
| Environments | Install compatible versions of neuroscience packages |
| Objects and classes | Read APIs in which recordings, epochs, and results are objects |
| Dictionaries | Store metadata, parameters, event mappings, and channel information |
| NumPy arrays | Represent data such as trials × channels × time |
| Axes and aggregation | Understand epoching, baseline correction, and evoked responses |
| Matplotlib | Inspect signals and communicate comparisons |

The most important mental habit is to annotate every array dimension with its scientific meaning.

## Natural Language Processing

Typical tasks include cleaning text, tokenisation, corpus exploration, vectorisation, and using learned representations.

| Foundation | Why it matters in NLP |
|---|---|
| Strings and lists | Represent documents, sentences, and tokens |
| Dictionaries | Represent documents, labels, vocabularies, and model inputs |
| Loops and comprehensions | Transform collections of documents |
| Functions | Make preprocessing steps reusable and testable |
| pandas | Explore corpora and metadata |
| Arrays and tensors | Represent documents × features or batch × tokens × embeddings |
| Objects and methods | Use vectorisers, tokenisers, pipelines, and models |

An NLP pipeline often begins with text and ends with numbers. At every step, ask what was preserved, removed, or encoded.

## Data Science, Prediction and Forecasting

The course covers statistical learning, regression, classification, resampling, regularisation, non-linear models, trees, support vector machines, and deep learning. Python is the working language that connects the data to those ideas.

| Foundation | Why it matters in Data Science |
|---|---|
| pandas | Clean, join, summarise, and inspect tabular data |
| NumPy | Understand numeric representations and dimensions |
| Functions | Build repeatable transformations and evaluation procedures |
| Objects and methods | Read the common `fit`, `predict`, and `transform` API |
| Boolean logic | Filter observations and define conditions correctly |
| Environments and seeds | Make analyses reproducible |
| Visualisation | Diagnose data and communicate model behaviour |

The central data structure is usually a feature matrix `X` with shape `samples × features`, accompanied by a target `y`.

## A shared example

These expressions come from different domains but use the same Python ideas:

```python
# ACN: trials × channels × time → channels × time
evoked = epochs.mean(axis=0)

# NLP: documents → document-term matrix
X_text = vectorizer.fit_transform(documents)

# Data Science: samples × features → fitted estimator
model.fit(X_train, y_train)
```

In each case, identify:

- the object on the left of the dot;
- the method being called;
- the arguments supplied;
- the type and shape of the returned object;
- the scientific interpretation of the transformation.

## What this workshop covers

The two days progress from language fundamentals to research workflows:

```text
values and types
    ↓
collections and control flow
    ↓
functions, objects, and files
    ↓
arrays, tables, and visualisation
    ↓
reproducible analysis and model workflows
```

You are not expected to memorise every method. You are expected to know how to inspect an object, consult documentation, test an assumption, and explain what your code does.

### Requested ACN preparation

| Requested topic | Where it appears |
|---|---|
| `pathlib` and project files | Environments and paths; setup diagnostic; capstone |
| Classes, objects, methods, and attributes | Python foundations; object-reading exercises; Matplotlib and scikit-learn APIs |
| Dictionaries | Python fundamentals; nested participant and acquisition metadata |
| Matplotlib | Evoked-response plots; accessibility notes; three figure challenges |
| Virtual environments | Full Conda/Anaconda and `venv` setup routes; VS Code kernel troubleshooting |
| 3D NumPy arrays | `epochs × channels × time`, indexing, aggregation, pseudo-epochs, and epoch-to-evoked challenge |
| Meaning of averaging an axis | Shape-prediction exercises, EEG notebook checks, and reflective questions about information loss |
