"""Live CodeQuiz prompts for the workshop.

Instructor: open this file after starting a session. Use the CodeLens actions
above each exercise to publish and reveal. Students receive a sanitised copy.
"""


# %% [codequiz]
# id: mutable-lists
# type: predict-output
# title: One list or two?
# prompt: Predict exactly what this program prints.
# tags: lists, mutation, objects

values = [1, 2, 3]
alias = values
alias.append(4)
print(values)

# %% [response]
expected_output = """
Write your prediction here.
"""

# %% [solution]
expected_output = "[1, 2, 3, 4]"

# %% [explanation]
# Both names refer to the same mutable list object.


# %% [codequiz]
# id: method-or-attribute
# type: predict-output
# title: Method or attribute?
# prompt: Which expression actually checks whether the file exists?
# tags: pathlib, objects, methods

from pathlib import Path

path = Path("data/trials.csv")

# A: path.exists
# B: path.exists()

# %% [response]
answer = ""

# %% [solution]
answer = "B: path.exists()"

# %% [explanation]
# path.exists is the method object. Parentheses call it and return a Boolean.


# %% [codequiz]
# id: epochs-axis
# type: predict-output
# title: Epochs to evoked
# prompt: What is the shape of evoked?
# tags: numpy, shapes, axes, neuroscience

import numpy as np

epochs = np.zeros((80, 32, 500))  # trials × channels × time
evoked = epochs.mean(axis=0)

# %% [response]
predicted_shape = ()

# %% [solution]
predicted_shape = (32, 500)

# %% [explanation]
# Averaging axis 0 removes the trial dimension and preserves channels × time.


# %% [codequiz]
# id: nlp-axis
# type: predict-output
# title: From token embeddings to document embeddings
# prompt: What shape remains after averaging axis 1?
# tags: numpy, shapes, nlp

embeddings = np.zeros((16, 128, 768))  # documents × tokens × features
documents = embeddings.mean(axis=1)

# %% [response]
predicted_shape = ()

# %% [solution]
predicted_shape = (16, 768)

# %% [explanation]
# Averaging tokens leaves one feature vector for every document.


# %% [codequiz]
# id: reusable-evoked
# type: code
# title: Make the analysis reusable
# prompt: Implement a function that returns one evoked channel.
# tags: functions, numpy, neuroscience

# %% [response]
def evoked_channel(epochs, channel):
    pass


# %% [solution]
def evoked_channel(epochs, channel):
    if epochs.ndim != 3:
        raise ValueError("Expected trials × channels × time")
    return epochs.mean(axis=0)[channel]

# %% [explanation]
# The function validates its assumption, averages trials, and selects one channel.
