# Notebooks

Open the repository in VS Code and select the workshop environment before running a notebook. Use **Shift+Enter** to run a cell.

## Notebook 0: Python warm-up

Lists, dictionaries, comprehensions, functions, debugging, and short written answers.

- {doc}`Open Notebook 0 <notebooks/00_python_warmup>` in the book
- {download}`Download Notebook 0 <notebooks/00_python_warmup.ipynb>`

## Notebook 1: Lexical decision data

Analyse trial-level reaction times and accuracy from a lexical-decision experiment.

- {doc}`Open Notebook 1 <notebooks/01_lexical_decision_pandas>` in the book
- {download}`Download Notebook 1 <notebooks/01_lexical_decision_pandas.ipynb>`
- {download}`Download the lexical-decision CSV <data/real/lexical_decision.csv>`

## Notebook 2: EEG arrays

Move between pandas and NumPy, select samples with Boolean masks, calculate channel means, and practise reshaping arrays.

- {doc}`Open Notebook 2 <notebooks/02_eeg_arrays>` in the book
- {download}`Download Notebook 2 <notebooks/02_eeg_arrays.ipynb>`
- {download}`Download the EEG Eye State data <data/real/eeg_eye_state.arff>`

## Notebook 3: Model workflow

Create participant-level features from lexical-decision trials, split at the participant
level, fit a scikit-learn pipeline, and inspect the confusion matrix and leakage risks.

- {doc}`Open Notebook 3 <notebooks/03_model_workflow>` in the book
- {download}`Download Notebook 3 <notebooks/03_model_workflow.ipynb>`

## Notebook 4: NLP text features

Build a document–term matrix and TF–IDF representation, compare documents, and transfer
NumPy axis reasoning to token embeddings.

- {doc}`Open Notebook 4 <notebooks/04_nlp_text_features>` in the book
- {download}`Download Notebook 4 <notebooks/04_nlp_text_features.ipynb>`

The checks compare selected values, shapes, or columns with expected results. Written interpretations are not checked automatically.

## Solutions

Try each exercise notebook first. When you need to compare your approach, use the
matching completed notebook:

- {download}`Notebook 0 solution <notebooks/solutions/00_python_warmup_solutions.ipynb>`
- {download}`Notebook 1 solution <notebooks/solutions/01_lexical_decision_pandas_solutions.ipynb>`
- {download}`Notebook 2 solution <notebooks/solutions/02_eeg_arrays_solutions.ipynb>`
- {download}`Notebook 3 solution <notebooks/solutions/03_model_workflow_solutions.ipynb>`
- {download}`Notebook 4 solution <notebooks/solutions/04_nlp_text_features_solutions.ipynb>`

In the repository, all completed notebooks are grouped under **`notebooks/solutions/`**.

## Data sources

The EEG Eye State data was donated by Oliver Roesler and is distributed by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/264/eeg%2Beye%2Bstate) under CC BY 4.0 ([DOI](https://doi.org/10.24432/C57G7J)).

The lexical-decision data is distributed with the [`languageR` package](https://cran.r-project.org/package=languageR) and described in Baayen's *Analyzing Linguistic Data: A Practical Introduction to Statistics* (2008). The package is licensed under GPL (≥ 2).
