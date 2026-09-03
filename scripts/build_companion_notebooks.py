"""Generate the student-facing workshop notebooks.

Run from the repository root with the book environment's Python.
"""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "notebooks"
OUTPUT.mkdir(parents=True, exist_ok=True)


FEEDBACK_CODE = '''
from pathlib import Path
import sys

# Find the repository from the notebook folder, solutions folder, or project root.
for _candidate in (Path.cwd().resolve(), *Path.cwd().resolve().parents):
    if (_candidate / "notebooks" / "workshop_checks.py").is_file():
        PROJECT_ROOT = _candidate
        break
else:
    raise FileNotFoundError(
        "Open this notebook inside the cloned workshop repository; "
        "notebooks/workshop_checks.py is required."
    )

sys.path.insert(0, str(PROJECT_ROOT / "notebooks"))

from workshop_checks import Check, run_checks

check = Check()
'''


def markdown(text):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text):
    return nbf.v4.new_code_cell(text.strip())


def hidden_code(text):
    cell = code(text)
    cell.metadata["tags"] = ["hide-input"]
    cell.metadata["jupyter"] = {"source_hidden": True}
    return cell


def hint(text):
    return markdown(
        f'''<details class="notebook-hint">
<summary><strong>Hint</strong></summary>

{text.strip()}

</details>'''
    )


def answer(text):
    return None


def discussion(text):
    return None


def notebook(title, cells):
    nb = nbf.v4.new_notebook()
    filtered = []
    for cell in cells:
        if cell is None:
            continue
        source = "".join(cell.get("source", []))
        if "Reflection" in source or "reflection_" in source:
            continue
        filtered.append(cell)
    nb["cells"] = [markdown(f"# {title}")] + filtered
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": "3.12"},
    }
    return nb


INTRO = notebook(
    "Notebook 0: Python warm-up",
    [
        markdown('''
Use these short exercises to practise basic Python patterns before the data notebooks.
Replace `...` where shown, run the check, and change one example to see what happens.
'''),
        hidden_code(FEEDBACK_CODE),
        markdown('''
## 1: Predict the output

What will this print? Choose `A`, `B`, or `C` before running the check.

```python
numbers = [1, 2]
alias = numbers
alias.append(3)
len(numbers)
```

- A: `2`
- B: `3`
- C: an error
'''),
        code('''answer_1 = ""  # replace with A, B, or C'''),
        hint('''Assignment gives two names to the same list. Appending through either name changes that list.'''),
        hidden_code('''run_checks("00_python_warmup_predict", locals())'''),
        markdown('''## 2: Use variables and arithmetic

Calculate the total cost for six items at seven units each.'''),
        code('''price = 7
quantity = 6
total = ...'''),
        hint('''Multiply `price` by `quantity`.'''),
        hidden_code('''run_checks("00_python_warmup_arithmetic", locals())'''),
        markdown('''## 3: Clean a string

Remove surrounding whitespace and make the word lowercase.'''),
        code('''word = "  PYTHON  "
clean_word = ...'''),
        hint('''Use `.strip()` and `.lower()`.'''),
        hidden_code('''run_checks("00_python_warmup_string", locals())'''),
        markdown('''## 4: Write a small function

Complete `is_even`. It should return `True` for even numbers and `False` for odd numbers.'''),
        code('''def is_even(number):
    ...'''),
        hint('''The remainder operator is `%`. An even number has remainder zero after division by two.'''),
        hidden_code('''run_checks("00_python_warmup_function", locals())'''),
        markdown('''## 5: Build a list with a comprehension

Create the squares of the numbers 1 through 4.'''),
        code('''squares = [number ** 2 for number in ...]'''),
        hint('''Use `range(1, 5)`.'''),
        hidden_code('''run_checks("00_python_warmup_list", locals())'''),
        markdown('''## 6: Read a dictionary

Select the value stored under the `course` key.'''),
        code('''person = {"name": "Ada", "course": "Python"}
course = ...'''),
        hint('''Use square brackets with the key name.'''),
        hidden_code('''run_checks("00_python_warmup_dictionary", locals())'''),
    ],
)


LEXICAL_DECISION = notebook(
    "Notebook 1: Lexical decision data with pandas",
    [
        markdown('''
The `lexdec` dataset contains 1,659 lexical-decision trials from 21 participants and 79
English nouns. Participants decided whether each stimulus was a word. The variables
include response accuracy, log reaction time, trial number, native-language group, word
frequency, word length, and semantic class.

Source: `languageR`, Baayen (2008).
'''),
        hidden_code(FEEDBACK_CODE),
        markdown("## 1: Load the data"),
        code('''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = PROJECT_ROOT / "book" / "data" / "real" / "lexical_decision.csv"
if not data_path.is_file():
    raise FileNotFoundError(f"Missing workshop data: {data_path}")

trials = ...  # load the CSV
trials.head()
'''),
        hint('''Use `pd.read_csv(data_path)`.'''),
        hidden_code('''
check.shape(trials, (1659, 28), hint="Read the CSV at data_path with pandas.")
'''),
        answer('''
```python
trials = pd.read_csv(data_path)
trials.head()
```
'''),
        markdown('''
## 2: Inspect the DataFrame

Inspect `.shape`, `.columns`, and `.dtypes`. Assign the number of trials, participants,
and words to the three variables below.
'''),
        code('''
print("shape:", trials.shape)
print("columns:", trials.columns.tolist())
print("types:\\n", trials.dtypes)

n_trials = ...
n_participants = ...
n_words = ...
'''),
        hint('''Use `len(trials)` for rows and `.nunique()` on `Subject` and `Word`.'''),
        hidden_code('''
check.equal(n_trials, 1659, hint="The first element of trials.shape is the number of rows.")
check.equal(n_participants, 21, hint="Count unique values in Subject with .nunique().")
check.equal(n_words, 79, hint="Count unique values in Word with .nunique().")
'''),
        answer('''
```python
n_trials = len(trials)
n_participants = trials["Subject"].nunique()
n_words = trials["Word"].nunique()
```
'''),
        markdown('''
## 3: Select columns

Create `analysis_columns` containing these columns in this order: `Subject`, `Word`,
`RT`, `NativeLanguage`, `Correct`, `Frequency`, `Length`, and `Class`.
'''),
        code('''
analysis_columns = ...
'''),
        hint('''Select multiple columns with `trials[["first", "second", ...]]`.'''),
        hidden_code('''
check.columns(
    analysis_columns,
    ["Subject", "Word", "RT", "NativeLanguage", "Correct", "Frequency", "Length", "Class"],
)
check.equal(len(analysis_columns), 1659, hint="Column selection should retain every trial.")
'''),
        answer('''
```python
analysis_columns = trials[[
    "Subject", "Word", "RT", "NativeLanguage",
    "Correct", "Frequency", "Length", "Class",
]]
```
'''),
        markdown('''
## 4: Accuracy and Boolean filtering

Count correct and incorrect responses. Then create `correct_trials` containing only
correct responses.
'''),
        code('''
n_correct = ...
n_incorrect = ...
correct_trials = ...
'''),
        hint('''Compare `trials["Correct"]` with the strings `"correct"` and `"incorrect"`. Use the resulting Boolean Series to filter rows.'''),
        hidden_code('''
check.equal(n_correct, 1594, hint="Use value_counts() or compare Correct with 'correct'.")
check.equal(n_incorrect, 65, hint="Use value_counts() or compare Correct with 'incorrect'.")
check.equal(set(correct_trials["Correct"]), {"correct"}, hint="Filter rows where Correct equals 'correct'.")
'''),
        answer('''
```python
n_correct = trials["Correct"].eq("correct").sum()
n_incorrect = trials["Correct"].eq("incorrect").sum()
correct_trials = trials.loc[trials["Correct"].eq("correct")]
```

There are 1,594 correct and 65 incorrect trials.
'''),
        markdown('''
### Reflection: What changes when errors disappear?

Filtering to correct responses is common in reaction-time analyses. Which research
question can `correct_trials` answer, and which question can it no longer answer? Could
the filter affect conditions or participant groups unequally?
'''),
        code('''
reflection_filtering = """
After filtering, the data can answer ...
It can no longer answer ...
"""
'''),
        discussion('''
The filtered data can describe response speed conditional on a correct answer. It
cannot describe accuracy or the complete speed–accuracy trade-off. If one group or
condition makes more errors, its remaining correct trials may be a selected subset, so
always inspect accuracy before interpreting reaction times.
'''),
        markdown('''
## 5: Convert reaction time

`RT` is the natural logarithm of reaction time in milliseconds. Add `RT_ms` to
`correct_trials` by applying `np.exp` to `RT`.
'''),
        code('''
correct_trials = correct_trials.copy()
correct_trials["RT_ms"] = ...
'''),
        hint('''The inverse of the natural logarithm is `np.exp`.'''),
        hidden_code('''
check.equal(
    round(float(correct_trials["RT_ms"].median()), 1),
    571.0,
    hint="Use np.exp(correct_trials['RT']).",
)
'''),
        answer('''
```python
correct_trials = correct_trials.copy()
correct_trials["RT_ms"] = np.exp(correct_trials["RT"])
```

The median correct-trial reaction time is approximately 571 ms.
'''),
        markdown('''
## 6: Summarise language groups

Calculate the median correct-trial reaction time for the two `NativeLanguage` groups.
Return a Series indexed by `NativeLanguage`.
'''),
        code('''
median_rt = ...
'''),
        hint('''Group by `NativeLanguage`, select `RT_ms`, and call `.median()`.'''),
        hidden_code('''
check.equal(round(float(median_rt.loc["English"]), 1), 541.5, hint="Group correct_trials by NativeLanguage and take the median of RT_ms.")
check.equal(round(float(median_rt.loc["Other"]), 1), 616.5, hint="Group correct_trials by NativeLanguage and take the median of RT_ms.")
'''),
        answer('''
```python
median_rt = (
    correct_trials
    .groupby("NativeLanguage")["RT_ms"]
    .median()
)
```

The medians are approximately 541.5 ms for the English group and 616.5 ms for the
Other group.
'''),
        markdown('''
### Reflection: One number per group

What does the group median conceal? Name two distributions or levels of variation you
would inspect before describing one language group as “slower.”
'''),
        code('''
reflection_group_summary = """
The median conceals ...
I would inspect ...
"""
'''),
        discussion('''
The two medians conceal variation between participants, variation between words, the
shape and tails of the reaction-time distributions, trial counts, and uncertainty.
Participant-level summaries and plots of the distributions are useful first checks;
an inferential analysis should respect repeated observations of participants and words.
'''),
        markdown('''
## 7: Word frequency and reaction time

Create one row per word with its frequency and mean correct reaction time. Plot word
frequency against mean reaction time.

Then answer:

1. What pattern is visible?
2. Why should the 1,659 trials not be treated as independent observations?
3. Which variables might confound a comparison between native-language groups?
'''),
        code('''
word_summary = ...

# Create a scatter plot of Frequency and mean_rt_ms.


# Interpretation:
'''),
        hint('''Group by `Word`, `Frequency`, and `Length` with `as_index=False`. Use named aggregation to create `mean_rt_ms`. Plot one point per row of the summary.'''),
        hidden_code('''
check.equal(len(word_summary), 79, hint="Group by Word, Frequency, and Length.")
check.columns(word_summary, ["Word", "Frequency", "Length", "mean_rt_ms"])
'''),
        answer('''
```python
word_summary = (
    correct_trials
    .groupby(["Word", "Frequency", "Length"], as_index=False)
    .agg(mean_rt_ms=("RT_ms", "mean"))
)

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(word_summary["Frequency"], word_summary["mean_rt_ms"], alpha=0.7)
ax.set(
    xlabel="Log word frequency",
    ylabel="Mean correct reaction time (ms)",
)
```

Higher-frequency words tend to have shorter reaction times. Trials are clustered within
participants and words, so the 1,659 rows are not independent. Word frequency, word
length, trial order, accuracy, and unequal participant composition could affect a simple
comparison between language groups.
'''),
        markdown('''
### Reflection: From pattern to claim

Write one sentence that the scatter plot supports and one stronger sentence that it
does **not** support. What additional analysis or design information would you need for
the stronger claim?
'''),
        code('''
reflection_claim = """
Supported: ...
Not supported: ...
I would need ...
"""
'''),
        discussion('''
The plot supports a descriptive statement such as “higher-frequency words tended to
have shorter mean reaction times in this dataset.” It does not by itself show that word
frequency caused faster responses. Word length, semantic class, participant effects,
and the sampling design would need attention in a model and interpretation.
'''),
    ],
)


EEG = notebook(
    "Notebook 2: EEG data: shapes, masks, and signals",
    [
        markdown('''
The UCI **EEG Eye State** dataset contains 14 EEG channels from one continuous
117-second measurement, with eye state labelled from video (`0` open, `1` closed).

It contains one participant and is not an `epochs × channels × time` dataset.

Roesler, O. (2013), UCI Machine Learning Repository, CC BY 4.0,
<https://doi.org/10.24432/C57G7J>.
'''),
        hidden_code(FEEDBACK_CODE),
        markdown("## 1: Load the ARFF file"),
        code('''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import arff

data_path = PROJECT_ROOT / "book" / "data" / "real" / "eeg_eye_state.arff"
if not data_path.is_file():
    raise FileNotFoundError(f"Missing workshop data: {data_path}")

raw_records, metadata = ...
eeg = ...
eeg["eyeDetection"] = ...
eeg.head()
'''),
        hint('''Use `arff.loadarff(data_path)`, pass the returned records to `pd.DataFrame`, and convert `eyeDetection` with `.astype(int)`.'''),
        hidden_code('''
check.shape(eeg, (14980, 15), hint="The completed DataFrame should have 14 channels and one label column.")
check.equal(str(eeg["eyeDetection"].dtype).startswith("int"), True, hint="Convert eyeDetection to integers.")
'''),
        answer('''
```python
raw_records, metadata = arff.loadarff(data_path)
eeg = pd.DataFrame(raw_records)
eeg["eyeDetection"] = eeg["eyeDetection"].astype(int)
eeg.head()
```
'''),
        markdown('''
## 2: Predict the shape

The dataset has 14 EEG channels and one label column. What is the shape of the complete
DataFrame?

- A: `(14980, 14)`
- B: `(14980, 15)`
- C: `(15, 14980)`
'''),
        code('''
answer_shape = ""
'''),
        hint('''Count the 14 EEG channels and the `eyeDetection` label column.'''),
        hidden_code('''
check.choice(
    answer_shape,
    "B",
    {
        "A": "That counts only features and forgets the target column.",
        "B": "",
        "C": "pandas uses rows × columns, not columns × rows.",
    },
)
'''),
        answer('''
**B: `(14980, 15)`.** The 14 channel columns plus `eyeDetection` give 15 columns.
The 14,980 measurements are rows.
'''),
        markdown("## 3: Separate features and target\n\nFill the blanks so `X` contains the channels and `y` contains eye state."),
        code('''
X = eeg.drop(columns=[...])
y = eeg[...]
'''),
        hint('''Remove `eyeDetection` from `X` and select that same column as `y`.'''),
        hidden_code('''
check.shape(X, (14980, 14), hint="Drop the eyeDetection label from the feature table.")
check.equal(y.name, "eyeDetection", hint="Select the label as a Series with one column name.")
'''),
        answer('''
```python
X = eeg.drop(columns=["eyeDetection"])
y = eeg["eyeDetection"]
```
'''),
        markdown('''
### Reflection: A target hiding among the features

Imagine leaving `eyeDetection` inside `X` before training a classifier to predict
`y`. What would happen to performance, and why would a very high score be a warning
rather than a success?
'''),
        code('''
reflection_leakage = """
Performance would ... because ...
"""
'''),
        discussion('''
The model would receive the answer as an input feature, so performance could become
nearly perfect without learning anything about EEG. This is target leakage. Suspiciously
strong results should prompt an inspection of feature names, preprocessing order, and
whether information from the target or test set entered the features.
'''),
        markdown('''
## 4: Move from pandas to NumPy

Create `signals` as a NumPy array. Then select the first 100 samples from channel O1.
The output should be one-dimensional.
'''),
        code('''
signals = ...
o1_index = list(X.columns).index("O1")
o1_excerpt = ...
'''),
        hint('''Use `.to_numpy()` for `signals`. Select rows `:100` and column `o1_index`.'''),
        hidden_code('''
check.shape(signals, (14980, 14))
check.shape(o1_excerpt, (100,), hint="Select rows 0:100 and one channel column.")
'''),
        answer('''
```python
signals = X.to_numpy()
o1_index = list(X.columns).index("O1")
o1_excerpt = signals[:100, o1_index]
```
'''),
        markdown('''
## 5: Boolean masks

Use `y` to make two arrays: samples recorded with eyes open and samples recorded with
eyes closed.
'''),
        code('''
eyes_open = ...
eyes_closed = ...
'''),
        hint('''`y.eq(0)` and `y.eq(1)` create Boolean row masks.'''),
        hidden_code('''
check.equal(eyes_open.shape[1], 14, hint="Use a Boolean row mask; retain every channel.")
check.equal(eyes_closed.shape[1], 14, hint="Use a Boolean row mask; retain every channel.")
check.equal(len(eyes_open) + len(eyes_closed), len(signals), hint="Every sample should belong to exactly one state.")
'''),
        answer('''
```python
eyes_open = signals[y.eq(0)]
eyes_closed = signals[y.eq(1)]
```
'''),
        markdown('''
## 6: Aggregate along the correct axis

Calculate one mean value per channel for each eye state. The result should have shape
`(14,)`.
'''),
        code('''
open_channel_means = ...
closed_channel_means = ...
'''),
        hint('''Rows contain measurements and columns contain channels. Average the row axis.'''),
        hidden_code('''
check.shape(open_channel_means, (14,), hint="Rows are samples. Which axis should disappear?")
check.shape(closed_channel_means, (14,), hint="Rows are samples. Which axis should disappear?")
'''),
        answer('''
```python
open_channel_means = eyes_open.mean(axis=0)
closed_channel_means = eyes_closed.mean(axis=0)
```

Axis 0 contains measurements. Averaging it leaves one mean per channel.
'''),
        markdown('''
### Reflection: What did the mean remove?

After averaging all samples within each eye state, which kinds of information are gone?
Could two recordings have identical channel means but meaningfully different signals?
Give one example.
'''),
        code('''
reflection_averaging = """
The mean removes ...
Two recordings could differ in ...
"""
'''),
        discussion('''
The means remove temporal order, transitions, variability, oscillatory structure, and
the distribution of values. Two recordings could share the same mean while differing
in variance, spectral power, artefacts, or the timing of state changes. Aggregation is
useful only when the retained summary matches the scientific question.
'''),
        markdown('''
## 7: Visual comparison

Make a grouped or paired plot comparing the 14 channel means. Label the axes and states.
Then answer: why would this plot alone be insufficient evidence that closing the eyes
*caused* the observed differences?
'''),
        code('''
# Create a grouped bar chart with one pair of bars per channel.


# Why this does not establish causation:
'''),
        hint('''Use `np.arange` for channel positions and offset the open/closed bars by half a bar width. Consider the number of participants, chronological dependence, artefacts, and experimental control.'''),
        answer('''
```python
channel_names = X.columns
positions = np.arange(len(channel_names))
width = 0.4

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(positions - width / 2, open_channel_means, width, label="Eyes open")
ax.bar(positions + width / 2, closed_channel_means, width, label="Eyes closed")
ax.set_xticks(positions, channel_names, rotation=45)
ax.set(xlabel="Channel", ylabel="Mean EEG value")
ax.legend()
plt.show()
```

The recording contains one participant and a chronological sequence rather than
independent, randomly assigned observations. Artefacts, drift, time, and transitions
between states could contribute to the difference. The plot is descriptive.
'''),
        markdown('''
## Bonus: Build pseudo-epochs

Take the first 14,000 samples and reshape them into
`100 pseudo-epochs × 140 time samples × 14 channels`, then transpose to the ACN
convention `epochs × channels × time`.

These fixed-width chunks are not experimentally defined epochs.
'''),
        code('''
pseudo_epochs = ...
'''),
        hint('''First reshape the first 14,000 rows to `(100, 140, 14)`, then transpose axes 1 and 2.'''),
        hidden_code('''
check.shape(pseudo_epochs, (100, 14, 140), hint="First reshape to (100, 140, 14), then transpose the final two axes.")
'''),
        answer('''
```python
pseudo_epochs = (
    signals[:14000]
    .reshape(100, 140, 14)
    .transpose(0, 2, 1)
)
```

The final shape is `pseudo-epochs × channels × time`: `(100, 14, 140)`.
'''),
        markdown('''
### Reflection: A valid shape is not yet a valid analysis

The pseudo-epochs have the expected three-dimensional shape. Why does that not make
them genuine experimental epochs? What event information would real epoching require?
'''),
        code('''
reflection_epoching = """
These chunks are not genuine epochs because ...
Real epoching would require ...
"""
'''),
        discussion('''
Reshaping creates equal-width chunks but does not align them to experimental events.
Real epoching needs event markers, event identities, a sampling rate, a defined time
window, and decisions about baselines, artefacts, and boundary cases. Correct dimensions
cannot replace experimental meaning.
'''),
    ],
)


MODEL_WORKFLOW = notebook(
    "Notebook 3: From behavioural summaries to a classifier",
    [
        markdown('''
This notebook uses the lexical-decision data again, but at a new unit of analysis:
one row per participant. The aim is to practise the scikit-learn interface and learn where leakage can enter an analysis.
'''),
        hidden_code(FEEDBACK_CODE),
        markdown("## 1: Load and prepare trial-level variables"),
        code('''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

data_path = PROJECT_ROOT / "book" / "data" / "real" / "lexical_decision.csv"
if not data_path.is_file():
    raise FileNotFoundError(f"Missing workshop data: {data_path}")

trials = ...
trials["is_correct"] = ...
trials["RT_ms"] = ...
'''),
        hint('''Load with `pd.read_csv`. Compare `Correct` with `"correct"`, and undo the natural logarithm in `RT` with `np.exp`.'''),
        hidden_code('''
check.shape(trials, (1659, 30))
check.equal(int(trials["is_correct"].sum()), 1594)
check.equal(round(float(trials["RT_ms"].median()), 1), 570.0)
'''),
        answer('''
```python
trials = pd.read_csv(data_path)
trials["is_correct"] = trials["Correct"].eq("correct")
trials["RT_ms"] = np.exp(trials["RT"])
```
'''),
        markdown('''
## 2: Make one row per participant

Create `participants` with `Subject` and `NativeLanguage`, plus mean reaction time,
accuracy, mean word frequency, and mean word length. Use named aggregation.
'''),
        code('''
participants = ...
participants.head()
'''),
        hint('''Group by `Subject` and `NativeLanguage` with `as_index=False`. Aggregate `RT_ms`, `is_correct`, `Frequency`, and `Length` with `.mean()`.'''),
        hidden_code('''
check.shape(participants, (21, 6))
check.columns(participants, ["Subject", "NativeLanguage", "mean_rt_ms", "accuracy", "mean_frequency", "mean_length"])
'''),
        answer('''
```python
participants = (
    trials.groupby(["Subject", "NativeLanguage"], as_index=False)
    .agg(
        mean_rt_ms=("RT_ms", "mean"),
        accuracy=("is_correct", "mean"),
        mean_frequency=("Frequency", "mean"),
        mean_length=("Length", "mean"),
    )
)
```
'''),
        markdown('''
## 3: Separate features and target

Let `X` contain the four numerical summaries and let `y` contain `NativeLanguage`.
'''),
        code('''
feature_names = ["mean_rt_ms", "accuracy", "mean_frequency", "mean_length"]
X = ...
y = ...
'''),
        hint('''Select the feature list with square brackets. Select the target with one column name so that it remains a Series.'''),
        hidden_code('''
check.shape(X, (21, 4))
check.shape(y, (21,))
check.equal(set(y), {"English", "Other"})
'''),
        answer('''
```python
X = participants[feature_names]
y = participants["NativeLanguage"]
```
'''),
        markdown('''
## 4: Split before learning preprocessing parameters

Use 30% of participants as a test set. Set `random_state=42` and stratify by `y`.
'''),
        code('''
X_train, X_test, y_train, y_test = ...
'''),
        hint('''Call `train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)`.'''),
        hidden_code('''
check.shape(X_train, (14, 4))
check.shape(X_test, (7, 4))
check.equal(set(y_train), {"English", "Other"})
'''),
        answer('''
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
```
'''),
        markdown('''
## 5: Fit a pipeline

Create a pipeline containing `StandardScaler()` followed by
`LogisticRegression(max_iter=1000)`. Fit it on the training rows and predict the test
rows.
'''),
        code('''
model = ...
model.fit(...)
predictions = ...  # predict the test rows
'''),
        hint('''Use `make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))`; then call `.fit(X_train, y_train)` and `.predict(X_test)`.'''),
        hidden_code('''
check.shape(predictions, (7,))
check.equal(set(predictions).issubset({"English", "Other"}), True)
'''),
        answer('''
```python
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000),
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
'''),
        markdown('''
## 6: Inspect the errors as well as the score

Create a 2 × 2 confusion matrix with labels ordered as `English`, `Other`. Then count
how many test predictions are correct.
'''),
        code('''
matrix = ...
n_correct_predictions = ...  # count matches
matrix
'''),
        hint('''Use `confusion_matrix(y_test, predictions, labels=["English", "Other"])`. Compare the two arrays and sum the Boolean results.'''),
        hidden_code('''
check.shape(matrix, (2, 2))
check.equal(int(matrix.sum()), 7)
check.equal(n_correct_predictions, int((predictions == y_test).sum()))
'''),
        answer('''
```python
matrix = confusion_matrix(
    y_test,
    predictions,
    labels=["English", "Other"],
)
n_correct_predictions = int((predictions == y_test).sum())
```

With only seven test participants, one changed prediction moves the accuracy by about
14 percentage points. Inspect the cases and sampling design rather than treating this
single split as a stable estimate.
'''),
        markdown('''
### Reflection: What would count as leakage here?

Name two ways information from the test participants could accidentally affect model
training. What part of the pipeline protects against one of them?
'''),
        code('''
reflection_model = """
Leakage could occur if ...
The pipeline protects against ...
"""
'''),
        discussion('''
Examples include scaling before the split, choosing features after examining test
performance, or allowing trials from the same participant to appear on both sides of a
trial-level split. The pipeline fits the scaler only on the training rows. It cannot
repair a split performed at the wrong unit or prevent decisions made after looking at
test results.
'''),
    ],
)


NLP_TEXT = notebook(
    "Notebook 4: Text to features",
    [
        markdown('''
Six short stories stand in for documents. The notebook follows the path from text to a document–term matrix, TF–IDF vectors, and a three-dimensional token representation.
'''),
        hidden_code(FEEDBACK_CODE),
        code('''
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "attention selects relevant visual information",
    "visual attention changes reaction time",
    "memory retrieval depends on context",
    "working memory supports language comprehension",
    "language models learn contextual representations",
    "reaction time measures lexical processing",
]
'''),
        markdown('''
## 1: Build a document–term matrix

Fit a `CountVectorizer` to `documents`. Store the sparse matrix in `counts` and the
feature names in `terms`.
'''),
        code('''
vectorizer = ...
counts = ...  # transform the documents
terms = ...
'''),
        hint('''Create `CountVectorizer()`, call `.fit_transform(documents)`, then call `.get_feature_names_out()` on the fitted vectorizer.'''),
        hidden_code('''
check.shape(counts, (6, 24))
check.equal(len(terms), 24)
check.equal("attention" in terms, True)
'''),
        answer('''
```python
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(documents)
terms = vectorizer.get_feature_names_out()
```
'''),
        markdown('''
## 2: Read the matrix

Calculate the number of counted tokens in each document. Then find the column index
for `reaction` and extract that column as a one-dimensional array.
'''),
        code('''
document_lengths = ...
reaction_index = ...
reaction_counts = ...  # extract one term column
'''),
        hint('''Sum `counts` across columns with `axis=1` and use `.A1` to obtain an array. Find a matching term with `list(terms).index(...)`; select that matrix column and use `.toarray().ravel()`.'''),
        hidden_code('''
check.equal(document_lengths.tolist(), [5, 5, 5, 5, 5, 5])
check.equal(reaction_counts.tolist(), [0, 1, 0, 0, 0, 1])
'''),
        answer('''
```python
document_lengths = counts.sum(axis=1).A1
reaction_index = list(terms).index("reaction")
reaction_counts = counts[:, reaction_index].toarray().ravel()
```
'''),
        markdown('''
## 3: TF–IDF and document similarity

Fit `TfidfVectorizer` and calculate the full document-by-document cosine-similarity
matrix.
'''),
        code('''
tfidf = ...
similarities = ...
'''),
        hint('''Use `TfidfVectorizer().fit_transform(documents)`, then pass the resulting matrix twice to `cosine_similarity`.'''),
        hidden_code('''
check.shape(tfidf, (6, 24))
check.shape(similarities, (6, 6))
check.equal(bool(np.allclose(np.diag(similarities), 1.0)), True)
'''),
        answer('''
```python
tfidf = TfidfVectorizer().fit_transform(documents)
similarities = cosine_similarity(tfidf, tfidf)
```

The diagonal is 1 because each document is identical to itself. Off-diagonal values
increase when documents share terms, weighted by how informative those terms are in
this small corpus.
'''),
        markdown('''
## 4: Transfer the axis reasoning to token vectors

The toy array below has shape `documents × tokens × embedding features`. Average over
tokens to create one vector per document.
'''),
        code('''
rng = np.random.default_rng(7)
token_vectors = rng.normal(size=(6, 8, 4))
document_vectors = ...
'''),
        hint('''Tokens are axis 1. Averaging that axis should leave `documents × embedding features`.'''),
        hidden_code('''
check.shape(document_vectors, (6, 4))
'''),
        answer('''
```python
document_vectors = token_vectors.mean(axis=1)
```

The token axis disappears, leaving one four-feature representation for each document.
'''),
        markdown('''
### Reflection: What did the representation forget?

Compare the document–term matrix with the averaged token vectors. What information is
absent from both? What additional information does the averaging operation discard?
'''),
        code('''
reflection_nlp = """
Both representations omit ...
Averaging also removes ...
"""
'''),
        discussion('''
A bag-of-words matrix omits word order and much syntax. Contextual token vectors may
encode order and context before aggregation, but a simple mean removes token position
and makes it impossible to recover which token contributed which feature. The right
representation depends on the linguistic question.
'''),
    ],
)


for filename, nb in {
    "00_python_warmup.ipynb": INTRO,
    "01_lexical_decision_pandas.ipynb": LEXICAL_DECISION,
    "02_eeg_arrays.ipynb": EEG,
    "03_model_workflow.ipynb": MODEL_WORKFLOW,
    "04_nlp_text_features.ipynb": NLP_TEXT,
}.items():
    nbf.write(nb, OUTPUT / filename)
    print(f"Wrote {OUTPUT / filename}")
