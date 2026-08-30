# Good coding practices and reusable scripts

A notebook is useful for exploring data. A script is useful when an analysis should
run the same way again: on another participant, on a remote computer, or next month.
It should make its inputs, steps, and outputs easy to find.

## From notebook cells to a script

A small script usually has four parts:

1. imports;
2. function definitions;
3. a `main()` function that connects the steps;
4. a main guard that starts the program.

```python
"""Summarise reaction times by participant and condition."""

from pathlib import Path

import pandas as pd


def load_trials(path):
    """Load a trial-level CSV file."""
    return pd.read_csv(path)


def summarise_trials(trials):
    """Return mean reaction time for each participant and condition."""
    required = {"participant", "condition", "reaction_time"}
    missing = required.difference(trials.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    return (
        trials
        .dropna(subset=["reaction_time"])
        .groupby(["participant", "condition"], as_index=False)
        .agg(mean_rt=("reaction_time", "mean"))
    )


def main():
    input_path = Path("data/trials.csv")
    output_path = Path("results/mean_reaction_times.csv")

    trials = load_trials(input_path)
    summary = summarise_trials(trials)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output_path, index=False)
    print(f"Saved {len(summary)} rows to {output_path}")


if __name__ == "__main__":
    main()
```

Run it from a terminal with:

```bash
python analyse_trials.py
```

The main guard means “run `main()` when this file is executed directly.” It does not
run `main()` when another file imports one of its functions. This makes the same code
both runnable and reusable.

## Define functions around meaningful steps

Give each function one clear job. A useful function normally:

- receives everything it needs through parameters;
- returns its result rather than hiding it in a global variable;
- has a descriptive verb-based name such as `load_trials` or `plot_accuracy`;
- checks important assumptions and fails with a helpful message;
- avoids changing its inputs unless mutation is part of its documented purpose.

```python
def exclude_fast_responses(trials, minimum_rt=0.2):
    """Return a copy containing responses at or above the RT threshold."""
    if minimum_rt < 0:
        raise ValueError("minimum_rt must be non-negative")
    return trials.loc[trials["reaction_time"] >= minimum_rt].copy()
```

Default values are useful when there is a sensible, visible default. Avoid placing
mutable objects such as lists or dictionaries in defaults. Use `None` instead:

```python
def select_conditions(trials, conditions=None):
    if conditions is None:
        conditions = ["congruent", "incongruent"]
    return trials.loc[trials["condition"].isin(conditions)].copy()
```

Docstrings explain the contract of reusable functions. Comments should explain
*why* a decision was made; the code itself should show *what* happens.

## Accept command-line arguments with `argparse`

Hard-coded paths make a script work for only one file. Command-line arguments turn
the script into a small tool:

```python
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Summarise reaction times by participant and condition."
    )
    parser.add_argument("input", type=Path, help="Trial-level CSV file")
    parser.add_argument("--output", type=Path, default=Path("results/summary.csv"))
    parser.add_argument(
        "--minimum-rt",
        type=float,
        default=0.2,
        help="Exclude faster responses in seconds (default: 0.2)",
    )
    return parser.parse_args()
```

Use the parsed values in `main()`:

```python
def main():
    args = parse_args()
    trials = load_trials(args.input)
    trials = exclude_fast_responses(trials, args.minimum_rt)
    summary = summarise_trials(trials)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)
```

Now the input can be **positional** because it is required, while output and threshold
are **optional flags** with defaults:

```bash
python analyse_trials.py data/trials.csv
python analyse_trials.py data/trials.csv --minimum-rt 0.3 --output results/strict.csv
python analyse_trials.py --help
```

Use flags for choices that benefit from names. For a true/false option, use an action:

```python
parser.add_argument(
    "--drop-incorrect",
    action="store_true",
    help="Exclude incorrect trials before summarising",
)
```

Do not use `type=bool`: text such as `"False"` can produce surprising results.

## Keep imports predictable

Put imports at the top of the file in three groups, separated by blank lines:

```python
import argparse                         # standard library
from pathlib import Path

import matplotlib.pyplot as plt         # third-party packages
import pandas as pd

from analysis.cleaning import clean_rt  # code from this project
```

Prefer explicit imports. They show readers where a name comes from:

```python
from pathlib import Path       # clear
import numpy as np             # conventional alias

from numpy import *            # avoid: origin of names is hidden
```

Import modules without triggering an analysis. File reading, plotting, and model
fitting belong in functions or `main()`, not at the top level. Never change
`sys.path` to make an import work; run code from the project root and organise shared
functions in an importable module or package instead.

## Separate decisions from machinery

Parameters describe analysis decisions; functions implement the work. Keeping them
separate makes decisions easier to review and change.

```python
def main():
    args = parse_args()
    summary = run_analysis(
        input_path=args.input,
        minimum_rt=args.minimum_rt,
        drop_incorrect=args.drop_incorrect,
    )
    save_summary(summary, args.output)
```

For a growing project, a simple layout might be:

```text
project/
├── data/                 # original inputs; do not edit by hand
├── results/              # generated tables and figures
├── analysis/
│   ├── __init__.py
│   ├── cleaning.py       # reusable functions
│   └── plotting.py
├── tests/
├── analyse_trials.py     # command-line entry point
├── README.md
└── requirements.txt      # recorded dependencies
```

## Errors, assertions, and messages

Use `ValueError`, `FileNotFoundError`, or another suitable exception when a caller
can supply invalid input. Reserve `assert` for internal assumptions and tests: Python
can disable assertions, so they should not validate user input.

```python
if not input_path.exists():
    raise FileNotFoundError(f"Input file not found: {input_path}")

assert not summary.duplicated(["participant", "condition"]).any()
```

Catch an exception only when you can add context, recover, or clean up. Avoid a bare
`except:` because it can hide spelling mistakes, keyboard interrupts, and real bugs.
For a short script, informative `print()` messages are fine. For longer pipelines,
Python's `logging` module provides levels and timestamps.

## A practical checklist

Before sharing or rerunning a script, check that:

- names describe the scientific meaning of values;
- paths use `pathlib.Path` and are not specific to one person's computer;
- analysis steps are functions with explicit inputs and returns;
- command-line options have types, defaults, and helpful descriptions;
- imports are explicit, grouped, and have no surprising side effects;
- raw data are read, not overwritten;
- outputs go to a deliberate location that the script creates if needed;
- random procedures use a recorded seed;
- dependencies and run instructions are recorded in `requirements.txt` and `README.md`;
- the command works from a fresh terminal and `python analyse_trials.py --help` is useful.

::::{exercise} Turn an analysis into a command-line tool
:label: script-refactor
Refactor the first script on this page so that it accepts an input CSV, an output
path, and an optional minimum reaction time. Run the script twice with different
thresholds and save the results under different names.
::::

::::{admonition} A sensible order
:class: dropdown
First move the threshold into a function parameter. Then add `parse_args()`. Finally,
connect the parsed values inside `main()` and inspect the output of `--help`.
::::

::::{solution} script-refactor
```python
"""Summarise reaction times from a trial-level CSV file."""

import argparse
from pathlib import Path

import pandas as pd


def load_trials(path):
    """Load a trial-level CSV file."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    return pd.read_csv(path)


def exclude_fast_responses(trials, minimum_rt=0.2):
    """Return trials at or above the reaction-time threshold."""
    if minimum_rt < 0:
        raise ValueError("minimum_rt must be non-negative")
    return trials.loc[trials["reaction_time"] >= minimum_rt].copy()


def summarise_trials(trials):
    """Return mean reaction time by participant and condition."""
    return (
        trials
        .dropna(subset=["reaction_time"])
        .groupby(["participant", "condition"], as_index=False)
        .agg(mean_rt=("reaction_time", "mean"))
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Summarise reaction times by participant and condition."
    )
    parser.add_argument("input", type=Path, help="Trial-level CSV file")
    parser.add_argument("--output", type=Path, required=True, help="Output CSV file")
    parser.add_argument(
        "--minimum-rt",
        type=float,
        default=0.2,
        help="Exclude faster responses in seconds (default: 0.2)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    trials = load_trials(args.input)
    trials = exclude_fast_responses(trials, args.minimum_rt)
    summary = summarise_trials(trials)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)
    print(f"Saved {len(summary)} rows to {args.output}")


if __name__ == "__main__":
    main()
```

For example, save two analyses without overwriting either result:

```bash
python analyse_trials.py data/trials.csv --minimum-rt 0.2 --output results/rt_200ms.csv
python analyse_trials.py data/trials.csv --minimum-rt 0.3 --output results/rt_300ms.csv
```
::::
