from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


project_dir = Path(__file__).resolve().parent.parent
trials_path = project_dir / "data" / "trials.csv"

trials = pd.read_csv(trials_path)

correct_trials = (
    trials
    .dropna(subset=["reaction_time"])
    .loc[lambda data: data["correct"]]
    .assign(reaction_time_ms=lambda data: data["reaction_time"] * 1000)
)

participant_summary = (
    correct_trials
    .groupby(["participant", "condition"], as_index=False)
    .agg(
        mean_rt_ms=("reaction_time_ms", "mean"),
        n_trials=("trial", "count"),
    )
    .sort_values(["participant", "condition"])
)

print(participant_summary)

condition_summary = (
    participant_summary
    .groupby("condition", as_index=False)
    .agg(
        mean_rt_ms=("mean_rt_ms", "mean"),
        variability=("mean_rt_ms", "std"),
    )
)

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(
    condition_summary["condition"],
    condition_summary["mean_rt_ms"],
    yerr=condition_summary["variability"],
    capsize=5,
)
ax.set(
    xlabel="Condition",
    ylabel="Mean reaction time (ms)",
    title="Correct-trial reaction time by condition",
)
fig.tight_layout()
plt.show()
