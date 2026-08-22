# Setup before the workshop

This guide sets up the workshop on your own laptop. If you would rather work in the
browser, Aarhus University also provides development environments through
[Interactive HPC on UCloud](https://interactivehpc.au.dk/en/about-interactive-hpc);
see the [UCloud user guide](https://docs.cloud.sdu.dk/) before launching an app.

Complete one route before Day 1. If a check fails and ChatGPT is not providing useful help, email szh@cc.au.dk.

## What you need

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the VS Code **Python** and **Jupyter** extensions.
3. Install the supplied **CodeQuiz Workshop** extension.
4. Download or clone this workshop repository from GitHub. See {doc}`resources/git_essentials` if you have not used Git before.
5. Choose **one** environment route below.

```{figure} _static/cartoons/xkcd-git.png
:alt: Three people discuss Git; one admits to relying on memorised commands and downloading a fresh copy after errors.
:width: 300px
:align: center

The commands in {doc}`resources/git_essentials` cover the Git operations used in this workshop. [“Git” by Randall Munroe](https://xkcd.com/1597/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

```{admonition} Choose one route
:class: important
Use either **Conda** or **`venv` + pip** for the workshop. Both create an isolated Python environment. Do not create a `venv` inside an activated Conda environment, and do not install the same project interchangeably through both approaches.

The Advanced Cognitive Neuroscience course recommends **Anaconda**. Installing
[Anaconda Distribution](https://www.anaconda.com/download) gives you Conda, Python,
Navigator, and the scientific package manager used by the course. The workshop
commands below work with Anaconda.
```

## What is an environment?

An environment contains the Python interpreter and packages used by one project. Isolation prevents one course from unexpectedly changing the package versions required by another.

```text
project
├── Python interpreter
├── NumPy
├── pandas
├── Matplotlib
└── other dependencies
```

Two commands answer two different questions:

```bash
python --version       # Which Python version is running?
python -m pip list     # Which packages are available to that Python?
```

Inside Python, the most reliable check is:

```python
import sys

print(sys.executable)
```

```{figure} _static/cartoons/xkcd-python-environment.png
:alt: A complicated stack of Python installations and package managers with a person installing another package at the bottom.
:width: 440px
:align: center

The reason this chapter insists on one environment at a time. [“Python Environment” by Randall Munroe](https://xkcd.com/1987/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

```{figure} _static/cartoons/xkcd-dependency.png
:alt: A course catalogue lists a class on dependency resolution as its own prerequisite.
:width: 340px
:align: center

Package dependencies can become circular too; an environment file records the set that worked together. [“Dependency” by Randall Munroe](https://xkcd.com/2347/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

## Route A: Conda or Anaconda

Conda manages both Python versions and packages. **Anaconda Distribution**, **Miniconda**, and **Miniforge** all provide the `conda` command:

- Anaconda includes many data-science packages and a graphical application called Navigator.
- Miniconda is a smaller installer from Anaconda.
- Miniforge is a smaller community installer configured for `conda-forge`.

The ACN course recommends a Conda environment for local MNE work because it includes compiled scientific and 3D dependencies.

### 1. Install Conda

Follow the [official Conda installation guide](https://docs.conda.io/projects/conda/en/stable/user-guide/install/). If you already have Anaconda, Miniconda, or Miniforge, you can skip this step.

After installation, close and reopen the terminal. Verify it:

```bash
conda --version
```

Windows users can run the commands in **Anaconda Prompt** if `conda` is not recognised in PowerShell.

### 2. Create the workshop environment

From the repository root, use the supplied environment file:

```bash
conda env create -f workshop-environment.yml
```

Activate it:

```bash
conda activate cogsci-python
```

The environment name should now appear at the beginning of the terminal prompt.

### Alternative: create it manually

```bash
conda create \
  --channel conda-forge \
  --strict-channel-priority \
  --name cogsci-python \
  python=3.12 \
  numpy pandas matplotlib seaborn scikit-learn \
  jupyterlab ipykernel
```

Then activate it:

```bash
conda activate cogsci-python
```

### 3. Make it available to Jupyter

```bash
python -m ipykernel install \
  --user \
  --name cogsci-python \
  --display-name "Python (cogsci-python)"
```

In a notebook, select **Python (cogsci-python)** as the kernel.

### 4. Update or recreate it

Update from the environment file:

```bash
conda env update \
  --name cogsci-python \
  --file workshop-environment.yml \
  --prune
```

Conda environments are disposable. If this one becomes inconsistent, remove and recreate it:

```bash
conda deactivate
conda env remove --name cogsci-python
conda env create -f workshop-environment.yml
```

## Route B: built-in `venv` and pip

`venv` is included with Python and creates a lightweight environment inside the project. It is a good default for the workshop and for projects whose dependencies install cleanly with pip.

### 1. Install Python

Install a current Python 3 release. Verify it in the terminal:

```bash
python --version
```

On some macOS or Linux systems, the command is `python3` instead. If so, substitute `python3` when creating the environment.

### 2. Create `.venv`

Open the repository folder in VS Code, open its terminal, and run:

```bash
python -m venv .venv
```

The `.venv` folder contains the environment. It should not be committed to Git or copied between computers.

### 3. Activate it

macOS or Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

The terminal prompt should now begin with `(.venv)`.

### 4. Install the workshop packages

```bash
python -m pip install --upgrade pip
python -m pip install -r workshop-requirements.txt
```

Using `python -m pip` makes it explicit that pip belongs to the currently selected Python interpreter.

### 5. Leave or recreate the environment

Leave it with:

```bash
deactivate
```

If the environment becomes inconsistent, delete only the `.venv` folder and repeat the creation and installation steps. Your scripts and data live outside `.venv` and are unaffected.

## Select the environment in VS Code

Environment activation in a terminal and interpreter selection in VS Code are related but separate.

1. Open the Command Palette with <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on macOS or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> on Windows/Linux.
2. Run **Python: Select Interpreter**.
3. Select either:
   - `.venv`, if you followed Route B; or
   - `cogsci-python`, if you followed Route A.
4. Open a new VS Code terminal after changing the interpreter.

The selected interpreter controls running, debugging, completion, and other Python features in VS Code. See the [official VS Code environment guide](https://code.visualstudio.com/docs/python/environments).

For notebooks, also click the kernel name in the upper-right corner and select the matching environment.

### If the interpreter or kernel is missing

First establish whether the environment itself works. Open a new VS Code terminal,
activate the environment, and run:

```bash
python -c "import sys; print(sys.executable)"
python -m pip show ipykernel
```

The first command should point into `.venv` or `cogsci-python`. If `ipykernel` is not
found, install and register it from that same activated environment:

```bash
python -m pip install ipykernel
python -m ipykernel install \
  --user \
  --name cogsci-python \
  --display-name "Python (cogsci-python)"
```

Then try these steps in order:

1. Run **Python: Select Interpreter** and choose the environment.
2. In the notebook, choose **Select Kernel → Python Environments** and select the same path.
3. Run **Developer: Reload Window** from the Command Palette.
4. Open a new notebook cell and compare `sys.executable` with the terminal result.

List the kernels Jupyter can currently see with:

```bash
jupyter kernelspec list
```

If Conda works in Anaconda Prompt but not in VS Code, close VS Code, reopen it after
Conda installation, and create a new terminal. On macOS or Linux, `conda init` followed
by restarting the shell may be necessary. Avoid installing packages repeatedly until
you have confirmed which interpreter the notebook is using.

## Run the diagnostic

Create `check_setup.py`:

```python
import sys
from pathlib import Path

import matplotlib
import numpy
import pandas
import sklearn

print("Python environment is ready")
print("Interpreter:", sys.executable)
print("Working directory:", Path.cwd())
print("NumPy:", numpy.__version__)
print("pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
print("scikit-learn:", sklearn.__version__)
```

Run it:

```bash
python check_setup.py
```

The interpreter path should contain either `.venv` or the Conda environment name `cogsci-python`.

```{admonition} Packages installed, but imports fail?
:class: warning
The terminal, editor, or notebook is probably using a different interpreter. Compare `sys.executable` in the failing context, then select the intended interpreter and kernel again.
```

## Optional ACN environment

The ACN repository uses a dedicated local environment with MNE and 3D visualisation support. Create this separately when the ACN course asks you to:

```bash
conda create \
  --channel conda-forge \
  --strict-channel-priority \
  --name mne_acn \
  python=3.12 \
  mne=1.10.0 \
  vtk=9.3 \
  pandas=2.3.1 \
  scikit-learn=1.7.1 \
  ipympl=0.9.7 \
  nibabel=5.3.2
```

```bash
conda activate mne_acn
```

This is a course-specific environment. Keep the general workshop environment separate so that changing an ACN dependency does not affect other work.

## Join CodeQuiz

On the workshop network:

1. Open the CodeQuiz activity-bar icon.
2. Select **Join session**.
3. Enter the six-character code shown by the instructor.
4. Exercises will open as editable Python scripts.
