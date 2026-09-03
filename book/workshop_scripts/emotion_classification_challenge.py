"""Explore how well a simple model recognises emotion labels in short comments."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "goemotions_workshop.csv"
RANDOM_SEED = 42


def load_data(path):
    """Load the workshop subset and validate its essential columns."""
    data = pd.read_csv(path)
    required = {"example_id", "source_id", "text", "emotion"}
    assert required.issubset(data.columns), "The dataset has unexpected columns"
    assert data[["text", "emotion"]].notna().all().all(), "Text or labels are missing"
    return data


def build_model():
    """Create a text-classification pipeline."""
    return make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), min_df=2),
        LogisticRegression(max_iter=1000),
    )


def make_error_table(example_ids, texts, actual, predicted):
    """Return only the incorrectly classified test examples."""
    results = pd.DataFrame(
        {
            "example_id": example_ids,
            "text": texts,
            "actual": actual,
            "predicted": predicted,
        }
    )
    return results.loc[results["actual"] != results["predicted"]]


if __name__ == "__main__":
    emotions = load_data(DATA_PATH)
    print("Dataset shape:", emotions.shape)
    print("\nExamples per label:\n", emotions["emotion"].value_counts())

    train, test = train_test_split(
        emotions,
        test_size=0.25,
        random_state=RANDOM_SEED,
        stratify=emotions["emotion"],
    )

    X_train = train["text"]
    y_train = train["emotion"]
    X_test = test["text"]
    y_test = test["emotion"]

    print("\nTraining text shape:", X_train.shape)
    print("Test text shape:", X_test.shape)

    model = build_model()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\nAccuracy:", round(accuracy_score(y_test, predictions), 3))
    print("\nClassification report:\n")
    print(classification_report(y_test, predictions))

    errors = make_error_table(
        example_ids=test["example_id"],
        texts=X_test,
        actual=y_test,
        predicted=predictions,
    )
    print("\nFirst ten errors:\n")
    print(errors.head(10).to_string(index=False))

    ConfusionMatrixDisplay.from_predictions(
        y_test,
        predictions,
        labels=model.classes_,
        cmap="Blues",
    )
    plt.title("Emotion predictions on held-out comments")
    plt.tight_layout()

    new_comments = [
        "I am delighted that everything worked out so well.",
        "The noise downstairs made me check every lock twice.",
        "Fine, I suppose that is exactly what I expected.",
        "I am sadly having the best day I have had all year.",
    ]
    print("\nPredictions for new comments:\n")
    for comment, label in zip(new_comments, model.predict(new_comments)):
        print(f"{label:>7}: {comment}")

    plt.show()
