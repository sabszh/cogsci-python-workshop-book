"""Create the small, classroom-screened GoEmotions subset used on Day 2."""

from argparse import ArgumentParser
from pathlib import Path
import re

import pandas as pd


TARGET_LABELS = {2: "anger", 14: "fear", 17: "joy", 25: "sadness"}
BLOCKED_PATTERN = re.compile(
    r"\b(?:fuck|shit|bitch|bastard|asshole|cunt|dick|pussy|porn|sex|suicide|"
    r"kill|murder|rape|racist|nazi|slut|whore|dead|death|died|dying|torture|"
    r"abuse|harass|bully|mental illness|self-harm|shoot|stab|religion|politic|"
    r"aspie|autis|retard|hell|damn|ass|crap|wtf|stupid|moron|idiot|meth|drug|alcohol|gun|knife|weapon|"
    r"rob|crime|violent|war|hatred|hate|pissed|suck|slug)\w*\b",
    flags=re.IGNORECASE,
)


def build_subset(source, output, examples_per_label=250, seed=42):
    """Select balanced, single-label, classroom-suitable examples."""
    data = pd.read_csv(
        source,
        sep="\t",
        header=None,
        names=["text", "label_ids", "source_id"],
        dtype=str,
    )

    single_label = data.loc[~data["label_ids"].str.contains(",")].copy()
    single_label["label_id"] = single_label["label_ids"].astype(int)
    selected = single_label.loc[single_label["label_id"].isin(TARGET_LABELS)].copy()
    selected["emotion"] = selected["label_id"].map(TARGET_LABELS)

    word_count = selected["text"].str.split().str.len()
    suitable = (
        word_count.between(5, 35)
        & ~selected["text"].str.contains(BLOCKED_PATTERN, na=False)
        & ~selected["text"].str.contains(r"https?://|www\.|/r/|/u/", case=False, regex=True)
    )
    selected = selected.loc[suitable, ["source_id", "text", "emotion"]]

    subset = (
        selected
        .groupby("emotion", group_keys=False)
        .sample(n=examples_per_label, random_state=seed)
        .sample(frac=1, random_state=seed)
        .reset_index(drop=True)
    )
    subset.insert(0, "example_id", [f"E{i:04d}" for i in range(1, len(subset) + 1)])

    output.parent.mkdir(parents=True, exist_ok=True)
    subset.to_csv(output, index=False)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--examples-per-label", type=int, default=250)
    parser.add_argument("--seed", type=int, default=42)
    arguments = parser.parse_args()
    build_subset(
        arguments.source,
        arguments.output,
        examples_per_label=arguments.examples_per_label,
        seed=arguments.seed,
    )
