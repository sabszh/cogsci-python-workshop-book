# Python fundamentals refresher

This chapter collects the language features used throughout the workshop. Treat it as a reference: skim what is familiar and pause where your prediction differs from Python's result.

After this chapter, use {doc}`../notebooks/00_python_warmup` to practise the same concepts in VS Code.

```{figure} ../_static/cartoons/xkcd-code-quality.png
:alt: A programmer reviews extremely confusing code and compares it with several increasingly absurd constructions.
:width: 620px
:align: center

Readable names and small functions make code easier to check six months after it was written. [“Code Quality” by Randall Munroe](https://xkcd.com/1513/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

## Names, values, and types

A variable is a name referring to an object:

```python
participant_id = "P07"
n_trials = 80
sampling_rate = 500.0
included = True
missing_value = None
```

Inspect rather than guess:

```python
type(participant_id)   # str
type(n_trials)        # int
type(sampling_rate)   # float
type(included)        # bool
```

Python is dynamically typed: the object has a type, while a name can later refer to a different object. Changing types without a good reason usually makes research code harder to follow.

```{admonition} Naming habit
:class: tip
Prefer names that carry scientific meaning: `reaction_times` is more informative than `x`, and `trial_axis` is more informative than `a`.
```

## Operators and comparisons

```python
duration = 500 / 1000       # division: 0.5
remainder = 17 % 5          # modulo: 2
squared = 3 ** 2            # exponentiation: 9

is_fast = duration < 0.7
is_valid = duration > 0 and duration < 2
```

Chained comparisons are idiomatic Python:

```python
is_valid = 0 < duration < 2
```

Use `==` to compare values and `=` to assign a name. Use `is None` when checking for the special singleton `None`.

## Strings

Strings are immutable sequences of characters:

```python
participant = "P07"
condition = "control"
label = f"{participant}_{condition}"

label.lower()
label.split("_")
label.replace("control", "experimental")
```

A method such as `.replace()` returns a new string; it does not modify the original.

```python
print(label)  # still P07_control
```

## Lists, tuples, sets, and dictionaries

Choose a collection based on its meaning:

| Type | Example | Use when |
|---|---|---|
| `list` | `[0.31, 0.28, 0.42]` | order matters and values may change |
| `tuple` | `(80, 32, 500)` | a fixed record or shape is useful |
| `set` | `{"A", "B"}` | membership or unique values matter |
| `dict` | `{"id": "P07", "age": 24}` | values have named keys |

Lists use integer positions:

```python
channels = ["Fz", "Cz", "Pz"]
channels[0]       # Fz
channels[-1]      # Pz
channels[1:]      # ["Cz", "Pz"]
```

Dictionaries use keys:

```python
participant = {"id": "P07", "age": 24, "included": True}
participant["age"]
participant.get("group", "unknown")
```

## Mutation and copying

<div class="live-python">
  <p><strong>Run it here:</strong> change the value appended to <code>alias</code>, then run the example again.</p>
  <textarea aria-label="Editable Python mutation example">values = [1, 2, 3]
alias = values
alias.append(4)
print(&quot;values:&quot;, values)
print(&quot;same object:&quot;, alias is values)</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

Some methods mutate an object:

```python
channels = ["Fz", "Cz"]
result = channels.append("Pz")

print(channels)  # ["Fz", "Cz", "Pz"]
print(result)    # None
```

This is a common source of confusion: `.append()` changes the list and returns `None`.

Assignment does not copy an object:

```python
first = [1, 2]
second = first
second.append(3)
print(first)  # [1, 2, 3]
```

Use `first.copy()` for a shallow copy. Nested mutable objects may require `copy.deepcopy()`.

```{admonition} Common mistake
:class: dropdown warning
`copy()` makes a shallow copy. Nested lists or dictionaries can still be shared by the
original and the copy. Check object identity with `is` when a change appears in two
places unexpectedly.
```

## Conditions

```python
if reaction_time <= 0:
    status = "invalid"
elif reaction_time < 0.7:
    status = "fast"
else:
    status = "slow"
```

Indentation defines the block. Four spaces is the standard.

Values such as `False`, `None`, `0`, `0.0`, `""`, and empty collections are *falsy*. Be explicit when zero and missing have different meanings.

## Loops and enumeration

Loop directly over values:

```python
for channel in channels:
    print(channel)
```

Use `enumerate` when both position and value are needed:

```python
for index, channel in enumerate(channels):
    print(index, channel)
```

Use `zip` for aligned collections:

```python
scores = [0.81, 0.76, 0.88]

for channel, score in zip(channels, scores):
    print(channel, score)
```

## Comprehensions

A comprehension constructs a collection from an iterable:

```python
channel_labels = [channel.lower() for channel in channels]
long_trials = [rt for rt in reaction_times if rt > 0.7]
squared = {number: number ** 2 for number in range(5)}
```

Use a normal loop if the comprehension becomes difficult to explain aloud.

## Functions

Functions give a transformation a name:

```python
def milliseconds_to_seconds(milliseconds):
    """Convert a duration in milliseconds to seconds."""
    return milliseconds / 1000
```

The docstring states the contract. The parameters are local names, and `return` sends a value back to the caller.

```python
seconds = milliseconds_to_seconds(450)
```

Default arguments should normally be immutable:

```python
def select_trials(trials, condition=None):
    if condition is None:
        return trials
    return trials[trials["condition"] == condition]
```

## Imports and namespaces

```python
import numpy as np
from pathlib import Path

values = np.array([1, 2, 3])
data_path = Path("data") / "trials.csv"
```

`np` is a conventional alias. `np.mean` and `Path` live in different namespaces, which makes their origin visible.

Avoid `from package import *`: it hides where names came from and can overwrite existing names.

## Exceptions

A traceback is a report, not merely a failure. The final line names the exception and usually provides the most useful first clue.

```python
def positive_mean(values):
    if len(values) == 0:
        raise ValueError("values must contain at least one observation")
    return sum(values) / len(values)
```

Raise an error when continuing would produce a misleading scientific result.

## A complete small example

```python
records = [
    {"participant": "P01", "condition": "A", "rt": 0.51, "correct": True},
    {"participant": "P01", "condition": "B", "rt": 0.73, "correct": True},
    {"participant": "P02", "condition": "A", "rt": 0.62, "correct": False},
]

def correct_reaction_times(records, condition):
    """Return RTs for correct trials in one condition."""
    return [
        record["rt"]
        for record in records
        if record["correct"] and record["condition"] == condition
    ]

condition_a = correct_reaction_times(records, "A")
mean_a = sum(condition_a) / len(condition_a)
print(f"Mean correct RT in A: {mean_a:.2f} seconds")
```

This short program uses lists, dictionaries, strings, Boolean expressions, a function, a comprehension, indexing, arithmetic, and formatted output. These are the same foundations later hidden inside larger scientific libraries.

::::{exercise} Predict before running
:label: fundamentals-predict
What do `condition_a` and `mean_a` contain? Which record is excluded, and why?
::::

::::{admonition} Hint
:class: dropdown
Both dictionary entries initially refer to the same `scores` list. A shallow
dictionary copy does not recursively copy nested lists.
::::

::::{solution} fundamentals-predict
`condition_a` is `[0.51]` and `mean_a` is `0.51`. The condition B record fails the condition check; the second condition A record fails the correctness check.
::::
