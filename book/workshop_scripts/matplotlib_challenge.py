"""Matplotlib figure remix: run this file in VS Code."""

import matplotlib.pyplot as plt
import numpy as np


conditions = np.array(["congruent", "incongruent", "neutral"])
participant_rt = np.array(
    [
        [502, 654, 541],
        [528, 702, 559],
        [491, 671, 530],
        [546, 725, 581],
        [509, 665, 548],
        [518, 690, 553],
        [497, 643, 535],
        [529, 698, 569],
    ]
)

mean_rt = participant_rt.mean(axis=0)
sem_rt = participant_rt.std(axis=0, ddof=1) / np.sqrt(participant_rt.shape[0])

# Your figure starts here. Replace or extend these lines.
fig, ax = plt.subplots(figsize=(7, 4))

# TODO: Choose a visual encoding for the participant values and/or condition means.
# TODO: Show uncertainty and add one useful annotation.
# TODO: Add a question or finding as the title, and label axes with units.
# TODO: Make the plot interpretable without colour alone.

fig.tight_layout()
plt.show()


# After the activity, compare your choices with this possible approach:
# fig, ax = plt.subplots(figsize=(7, 4))
# for row in participant_rt:
#     ax.plot(conditions, row, color="0.78", linewidth=1, marker="o", markersize=3)
# ax.errorbar(conditions, mean_rt, yerr=sem_rt, color="#332288",
#             linewidth=2.5, marker="o", capsize=5, label="Mean ± SEM")
# difference = mean_rt[1] - mean_rt[0]
# ax.annotate(f"Interference: +{difference:.0f} ms", xy=(1, mean_rt[1]),
#             xytext=(1.18, mean_rt[1] + 20),
#             arrowprops={"arrowstyle": "->"})
# ax.set(title="Does conflicting colour information slow responses?",
#        xlabel="Stroop condition", ylabel="Reaction time (ms)")
# ax.spines[["top", "right"]].set_visible(False)
# fig.tight_layout()
# fig.savefig("stroop_remix.png", dpi=160, bbox_inches="tight")
