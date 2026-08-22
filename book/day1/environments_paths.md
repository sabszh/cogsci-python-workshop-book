# Environments and paths

A **path** is an address for a file or folder. Research scripts use paths to locate raw
data, configuration files, saved arrays, figures, and output tables. A path that only
works from one person's Desktop is one of the most common reasons an analysis fails on
another computer.

This chapter separates two questions: *which Python and packages execute the script?*
and *which files does the script read?* Environments answer the first; paths answer the
second.

Before continuing, make sure you have completed one of the two environment routes in {doc}`../setup`: **Conda** or **`venv` + pip**.

## Conda and venv solve the same core problem

| | Conda | `venv` + pip |
|---|---|---|
| Creates isolated environments | yes | yes |
| Selects a Python version | yes | uses an installed Python |
| Installs Python packages | `conda install` | `python -m pip install` |
| Can manage non-Python libraries | yes | no |
| Common environment location | central Conda directory | `.venv` inside the project |
| Useful here | ACN/MNE and compiled dependencies | lightweight general workshop setup |

Neither tool makes an analysis reproducible by itself. Reproducibility comes from recording the packages in a file such as `workshop-environment.yml` or `workshop-requirements.txt` and testing that the environment can be recreated.

## Three locations to distinguish

```{admonition} Common mistake
:class: dropdown warning
Opening the correct project folder does not automatically select its Python
interpreter. Check the interpreter shown in the VS Code status bar and compare
`sys.executable` with the environment you intended to use.
```

These locations are related but not interchangeable. The Python interpreter is an
executable program. An environment is the interpreter plus its installed packages.
The working directory is the folder Python treats as the starting point for a relative
file address.

```text
Python interpreter  → which Python runs?
Environment         → which packages are installed?
Working directory   → where do relative paths begin?
```

Inspect them:

```python
import sys
from pathlib import Path

print("Interpreter:", sys.executable)
print("Working directory:", Path.cwd())
```

`Path.cwd()` returns the current working directory as a `Path` object. It may change
depending on whether code is launched from a terminal, VS Code's Run button, or a
notebook. This is why a relative path can work in one context and fail in another.

## Building a path with `Path`

`Path` represents a filesystem address as an object. The `/` operator joins path
components; it does not divide numbers here because `Path` defines a path-specific
meaning for that operator.

Read the next example one line at a time:

- `Path.cwd()` supplies the starting folder.
- `project / "data"` appends a folder named `data`.
- the f-string inserts the participant ID into a filename.
- the final `/` appends that filename to the data folder.

No folder or file is created by these expressions. They only construct an address.

```python
from pathlib import Path

project = Path.cwd()
data_dir = project / "data"
participant_id = "P07"
epochs_file = data_dir / f"{participant_id}_epochs.npy"

print(epochs_file)
print(epochs_file.exists())
```

If the working directory is `/Users/name/project`, the resulting value is equivalent
to `/Users/name/project/data/P07_epochs.npy` on macOS. On Windows, `Path` uses the
appropriate drive and separators automatically.

Avoid string assembly such as:

```python
epochs_file = str(project) + "/data/" + participant_id + "_epochs.npy"
```

That version mixes path logic with string formatting and assumes a separator. Keeping
the value as a `Path` also gives access to filesystem methods.

Useful attributes and methods:

```python
epochs_file.name
epochs_file.stem
epochs_file.suffix
epochs_file.parent
epochs_file.with_suffix(".csv")
```

<div class="live-python">
  <p><strong>Check with Python:</strong> edit the participant ID or suffix and inspect the resulting path.</p>
  <textarea aria-label="Editable pathlib example">from pathlib import Path
project = Path(&quot;workshop&quot;)
participant_id = &quot;P07&quot;
epochs_file = project / &quot;data&quot; / f&quot;{participant_id}_epochs.npy&quot;
print(&quot;path:&quot;, epochs_file)
print(&quot;name:&quot;, epochs_file.name)
print(&quot;CSV version:&quot;, epochs_file.with_suffix(&quot;.csv&quot;))</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

Attributes such as `.name`, `.stem`, `.suffix`, and `.parent` describe the address and
do not use parentheses. Methods such as `.exists()` and `.with_suffix()` perform an
operation and therefore use parentheses. `.with_suffix(".csv")` returns a new path; it
does not rename the original file.

## Find collections of files

`glob` searches a folder for names matching a pattern. In `*_epochs.npy`, `*` means
“any sequence of characters,” so the pattern matches `P01_epochs.npy` and
`P07_epochs.npy`, but not `participants.csv`. `glob` returns an iterable of `Path`
objects; `sorted` makes their order deterministic.

```python
epoch_files = sorted(data_dir.glob("*_epochs.npy"))

for path in epoch_files:
    print(path.stem)
```

::::{exercise} Robust project path
:label: path-project
Suppose `analysis.py` lives inside `src/`, while data lives in `data/` beside `src/`. Construct `data/trials.csv` relative to the script, not relative to wherever the user launched Python.
::::

::::{admonition} Hint
:class: dropdown
Start from `Path(__file__).resolve()`. The script lives inside `src`, so move to its
parent directory before appending `data/trials.csv`.
::::

::::{solution} path-project
```python
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
trials_path = project_dir / "data" / "trials.csv"
```

`__file__` is the path of the running script. `.resolve()` makes it absolute, the first
`.parent` moves from `analysis.py` to `src`, and the second moves from `src` to the
project folder. Notebooks do not define `__file__`; in a notebook, use a known project
root or locate it from `Path.cwd()` after checking the current directory.
::::
