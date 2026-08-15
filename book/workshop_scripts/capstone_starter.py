"""Starter for the integrated Cognitive Science challenge."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


def load_data():
    """Load trial and participant tables."""
    trials = pd.read_csv(DATA_DIR / "trials.csv")
    participants = pd.read_csv(DATA_DIR / "participants.csv")
    return trials, participants


def simulate_epochs(seed=42):
    """Return two arrays shaped trials × channels × time."""
    rng = np.random.default_rng(seed)
    epochs_a = rng.normal(size=(60, 8, 300))
    epochs_b = rng.normal(size=(60, 8, 300))
    epochs_b[:, 2, 140:180] += 0.6
    return epochs_a, epochs_b


def summarise_behaviour(trials):
    """TODO: return participant × condition summaries."""
    raise NotImplementedError


def compute_evoked(epochs):
    """TODO: average over trials after validating shape."""
    raise NotImplementedError


def plot_channel(evoked_a, evoked_b, channel=2):
    """TODO: plot both conditions and their difference."""
    raise NotImplementedError


if __name__ == "__main__":
    trials, participants = load_data()
    epochs_a, epochs_b = simulate_epochs()

    print("Trials:", trials.shape)
    print("Participants:", participants.shape)
    print("Epochs A:", epochs_a.shape)
