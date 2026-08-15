# Workshop recap

The first two workshop days move from individual Python objects to complete analysis
steps. The recurring questions are: **What object do I have? What does each dimension
or column mean? What transformation am I applying? What should the result contain?**

## Python foundations

| Topic | What to remember |
|---|---|
| Values and types | A name points to an object. Use `type()` when an operation behaves unexpectedly. |
| Collections | Lists preserve order; dictionaries connect meaningful keys to values; sets store unique values; tuples are fixed sequences. |
| Mutation and copying | Two names can refer to the same mutable object. A method such as `.append()` may therefore affect both names. |
| Control flow | Conditions select a branch; loops repeat an operation; comprehensions build collections compactly. |
| Functions | Give each function explicit inputs and a clear return value. Separate calculation from printing or saving where possible. |
| Objects | An **attribute** stores information; a **method** performs an operation. Inspect unfamiliar objects with `type()`, `dir()`, `help()`, and their documentation. |
| Errors | Read the final traceback line first, inspect the relevant object, and reduce the problem to a small example. |

## Projects, environments, and files

- A Python environment determines which interpreter and packages are available.
- Conda and `venv` solve the same core isolation problem in different ways.
- VS Code and Jupyter must use the interpreter or kernel belonging to the intended environment.
- `Path.cwd()` reports the working directory; it is not necessarily the directory containing a script.
- Build file locations with `pathlib.Path` and `/`, for example `project / "data" / "trials.csv"`.
- Check paths with `.exists()`, inspect their parts with `.name`, `.suffix`, and `.parent`, and find sets of files with `.glob()`.

## Arrays, tables, and figures

### NumPy

For an array shaped `trials × channels × time`, write the meaning beside every axis
before indexing or averaging.

- Integer indexing removes the selected dimension.
- `.mean(axis=n)` removes axis `n` unless `keepdims=True`.
- Averaging trials converts `trials × channels × time` into `channels × time`.
- Broadcasting works by comparing dimensions from right to left; dimensions must match or have size one.
- Print `.shape` before and after an important transformation.

### pandas

- Inspect columns, types, missing values, and the unit represented by one row before transforming data.
- A Boolean expression creates a mask for selecting rows.
- `groupby()` changes the unit of analysis; state what one row means after aggregation.
- Treat missing observations explicitly rather than allowing them to disappear unnoticed.
- Check join keys and row counts before and after `merge()`.

### Matplotlib

- Create figures explicitly with `fig, ax = plt.subplots()`.
- The lengths and shapes of plotted values must agree.
- Label axes with the measured variable and its unit.
- Show individual observations or uncertainty when these matter for interpretation.
- Do not rely on colour alone; use accessible colours together with markers, line styles, or direct labels.

## From analysis steps to models

Functions make a processing step reusable and testable. Assertions record conditions
that must hold, such as expected columns or array shapes. Together they make it easier
to identify the exact step at which data stop matching expectations.

The model workflow introduced on Day 2 is:

1. define samples, features `X`, and target `y`;
2. split training and test observations before learning from the data;
3. place learned preprocessing inside a pipeline;
4. call `.fit()` on training data;
5. call `.predict()` or `.score()` on held-out data;
6. inspect errors and limitations, not only the final score.

Scaling, feature selection, or vocabulary construction performed before the split can
leak information from the test set. A random seed makes a result repeatable; it does
not make the design or interpretation valid.

## Connections to the MSc courses

| Course | Workshop ideas that transfer directly |
|---|---|
| Advanced Cognitive Neuroscience | Environments, paths, object APIs, dictionaries, 3D arrays, epochs and evoked responses, axes, and Matplotlib. |
| Natural Language Processing | Dictionaries containing text and labels, preprocessing functions, document–feature matrices, model objects, and token-tensor shapes. |
| Data Science, Prediction and Forecasting | pandas transformations, samples and features, train/test splits, scikit-learn estimators, pipelines, evaluation, and leakage. |

## Notebook map

- **Notebook 0:** Python collections, functions, mutation, and debugging.
- **Notebook 1:** lexical-decision data with pandas.
- **Notebook 2:** EEG data, masks, shapes, and array operations.
- **Notebook 3:** participant summaries, classification, pipelines, and leakage.
- **Notebook 4:** text preprocessing, count and TF–IDF features, and embedding dimensions.

## Before trusting an analysis

Ask these questions at each important step:

1. What is the object's type?
2. What does one row or each array dimension represent?
3. Are missing values and exclusions visible?
4. Did the operation mutate an existing object or create a new one?
5. What changed in the shape, columns, or unit of analysis?
6. Has information from the test data entered model training?
7. Does the figure or score support the scientific claim being made?
8. Could another person run the project with the recorded environment and paths?

## Day 3

Day 3 will address responsible use of generative AI and will be accompanied by a new
notebook. Its detailed content is still being developed.
