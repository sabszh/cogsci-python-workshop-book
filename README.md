# Python for Cognitive Science

A two-day interactive Python refresher for incoming MSc Cognitive Science students. The material prepares students for Advanced Cognitive Neuroscience, Natural Language Processing, and Data Science, Prediction and Forecasting.

## Open the workshop files

Clone or download the repository, then open the repository folder—not an individual
file—in VS Code. Student-facing material is organised as follows:

```text
cogsci-python-workshop/
├── book/
│   ├── notebooks/          # five exercise notebooks
│   ├── workshop_scripts/   # CodeQuiz, Matplotlib, and capstone scripts
│   ├── data/               # CSV and EEG files used by the exercises
│   ├── day1/               # Day 1 booklet chapters
│   └── day2/               # Day 2 booklet chapters
├── workshop-environment.yml
└── workshop-requirements.txt
```

In VS Code:

1. Select the workshop Python interpreter.
2. Open `book/notebooks/` for notebook exercises.
3. Open `book/workshop_scripts/` for editable `.py` activities.
4. Keep files in their folders so relative data paths continue to work.

## Build locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter-book build book
```

Open `book/_build/html/index.html` after the build.

## Publish with GitHub Pages

1. Create a GitHub repository and push this directory.
2. In **Settings → Pages**, select **GitHub Actions** as the source.
3. Replace the placeholder repository URL and base URL in `book/_config.yml`.
4. Push to `main`. The included workflow builds and deploys the book.

## Content

- Day 1: environments, paths, objects, dictionaries, NumPy dimensions, and visualisation
- Day 2: functions, pandas, model workflows, NLP data structures, and an integrated challenge
- Instructor guide and CodeQuiz prompts
- Downloadable workshop scripts and sample data

Students install only `workshop-requirements.txt`. The root `requirements.txt` additionally contains the documentation build dependencies.

Workshop text and original material are licensed CC BY 4.0. The xkcd
images in `book/_static/cartoons/` are by Randall Munroe and are separately
licensed CC BY-NC 2.5; each use is attributed in the book.
