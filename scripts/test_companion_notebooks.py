"""Execute reference-completed copies of the workshop notebooks."""

from __future__ import annotations

import copy
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


REPLACEMENTS = {
    "00_python_warmup.ipynb": {
        'answer_1 = ""  # replace with A, B, or C': 'answer_1 = "B"',
        'total = ...': 'total = price * quantity',
        'clean_word = ...': 'clean_word = word.strip().lower()',
        '''def is_even(number):
    ...''': '''def is_even(number):
    return number % 2 == 0''',
        'squares = [number ** 2 for number in ...]':
            'squares = [number ** 2 for number in range(1, 5)]',
        'course = ...': 'course = person["course"]',
    },
    "01_lexical_decision_pandas.ipynb": {
                "trials = ...  # load the CSV": "trials = pd.read_csv(data_path)",
        "n_trials = ...": "n_trials = len(trials)",
        "n_participants = ...": 'n_participants = trials["Subject"].nunique()',
        "n_words = ...": 'n_words = trials["Word"].nunique()',
        "analysis_columns = ...": '''analysis_columns = trials[[
    "Subject", "Word", "RT", "NativeLanguage",
    "Correct", "Frequency", "Length", "Class",
]]''',
        "n_correct = ...": 'n_correct = trials["Correct"].eq("correct").sum()',
        "n_incorrect = ...": 'n_incorrect = trials["Correct"].eq("incorrect").sum()',
        "correct_trials = ...": 'correct_trials = trials.loc[trials["Correct"].eq("correct")]' ,
        'correct_trials["RT_ms"] = ...': 'correct_trials["RT_ms"] = np.exp(correct_trials["RT"])',
        "median_rt = ...": 'median_rt = correct_trials.groupby("NativeLanguage")["RT_ms"].median()',
        "word_summary = ...": '''word_summary = (
    correct_trials
    .groupby(["Word", "Frequency", "Length"], as_index=False)
    .agg(mean_rt_ms=("RT_ms", "mean"))
)''',
    },
    "02_eeg_arrays.ipynb": {
        "raw_records, metadata = ...": "raw_records, metadata = arff.loadarff(data_path)",
        "eeg = ...": "eeg = pd.DataFrame(raw_records)",
        'eeg["eyeDetection"] = ...': 'eeg["eyeDetection"] = eeg["eyeDetection"].astype(int)',
        'answer_shape = ""': 'answer_shape = "B"',
        'X = eeg.drop(columns=[...])': 'X = eeg.drop(columns=["eyeDetection"])',
        'y = eeg[...]': 'y = eeg["eyeDetection"]',
        'signals = ...': 'signals = X.to_numpy()',
        'o1_excerpt = ...': 'o1_excerpt = signals[:100, o1_index]',
        'eyes_open = ...': 'eyes_open = signals[y.eq(0)]',
        'eyes_closed = ...': 'eyes_closed = signals[y.eq(1)]',
        'open_channel_means = ...': 'open_channel_means = eyes_open.mean(axis=0)',
        'closed_channel_means = ...': 'closed_channel_means = eyes_closed.mean(axis=0)',
        'pseudo_epochs = ...': 'pseudo_epochs = signals[:14000].reshape(100, 140, 14).transpose(0, 2, 1)',
    },
    "03_model_workflow.ipynb": {
        "trials = ...": "trials = pd.read_csv(data_path)",
        'trials["is_correct"] = ...': 'trials["is_correct"] = trials["Correct"].eq("correct")',
        'trials["RT_ms"] = ...': 'trials["RT_ms"] = np.exp(trials["RT"])',
        "participants = ...": '''participants = (
    trials.groupby(["Subject", "NativeLanguage"], as_index=False)
    .agg(
        mean_rt_ms=("RT_ms", "mean"),
        accuracy=("is_correct", "mean"),
        mean_frequency=("Frequency", "mean"),
        mean_length=("Length", "mean"),
    )
)''',
        "X = ...": "X = participants[feature_names]",
        "y = ...": 'y = participants["NativeLanguage"]',
        "X_train, X_test, y_train, y_test = ...": '''X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)''',
        "model = ...": '''model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000),
)''',
        "model.fit(...)": "model.fit(X_train, y_train)",
        "predictions = ...  # predict the test rows": "predictions = model.predict(X_test)",
        "matrix = ...": '''matrix = confusion_matrix(
    y_test, predictions, labels=["English", "Other"]
)''',
        "n_correct_predictions = ...  # count matches": "n_correct_predictions = int((predictions == y_test).sum())",
    },
    "04_nlp_text_features.ipynb": {
        "vectorizer = ...": "vectorizer = CountVectorizer()",
        "counts = ...  # transform the documents": "counts = vectorizer.fit_transform(documents)",
        "terms = ...": "terms = vectorizer.get_feature_names_out()",
        "document_lengths = ...": "document_lengths = counts.sum(axis=1).A1",
        "reaction_index = ...": 'reaction_index = list(terms).index("reaction")',
        "reaction_counts = ...  # extract one term column": "reaction_counts = counts[:, reaction_index].toarray().ravel()",
        "tfidf = ...": "tfidf = TfidfVectorizer().fit_transform(documents)",
        "similarities = ...": "similarities = cosine_similarity(tfidf, tfidf)",
        "document_vectors = ...": "document_vectors = token_vectors.mean(axis=1)",
    },
}


def complete_notebook(path: Path):
    notebook = nbformat.read(path, as_version=4)
    completed = copy.deepcopy(notebook)
    replacements = REPLACEMENTS[path.name]
    applied = {original: 0 for original in replacements}

    for cell in completed.cells:
        if cell.cell_type != "code":
            continue
        for original, replacement in replacements.items():
            if original in cell.source:
                cell.source = cell.source.replace(original, replacement)
                applied[original] += 1

    missing = [original for original, count in applied.items() if count != 1]
    if missing:
        raise AssertionError(
            f"{path.name}: expected each reference replacement once; failed for {missing}"
        )

    return completed


def output_text(notebook) -> str:
    pieces = []
    for cell in notebook.cells:
        for output in cell.get("outputs", []):
            if output.output_type == "stream":
                pieces.append(output.text)
            elif output.output_type == "error":
                pieces.append("\n".join(output.traceback))
    return "\n".join(pieces)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="cogsci-notebook-tests-") as temp_dir:
        temp_path = Path(temp_dir)

        cases = []
        for filename in REPLACEMENTS:
            student = NOTEBOOKS / filename
            solution = NOTEBOOKS / "solutions" / filename.replace(".ipynb", "_solutions.ipynb")
            for source in (student, solution):
                for working_dir in (ROOT, source.parent):
                    cases.append((source, working_dir))

        for source, working_dir in cases:
            completed = (
                complete_notebook(source)
                if source.parent == NOTEBOOKS
                else nbformat.read(source, as_version=4)
            )
            client = NotebookClient(
                completed,
                timeout=120,
                kernel_name="python3",
                resources={"metadata": {"path": str(working_dir)}},
            )
            executed = client.execute()
            text = output_text(executed)

            if "✗" in text:
                raise AssertionError(f"{source.name}: at least one exercise check failed\n{text}")

            destination = temp_path / source.name
            nbformat.write(executed, destination)
            passed = text.count("✅")
            print(
                f"{source.name} from {working_dir.relative_to(ROOT)}: "
                f"executed successfully ({passed} checks passed)", flush=True
            )


if __name__ == "__main__":
    main()
