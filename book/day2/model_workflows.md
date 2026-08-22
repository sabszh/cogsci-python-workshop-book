# The shared model workflow

Data Science covers regression, classification, regularised linear models, decision
trees, support vector machines, and neural networks. These approaches differ in what
relationships they can represent, how they are fitted, and how their predictions are
interpreted. In scikit-learn, however, they are often used through the same small set of
methods: create an estimator, call `.fit()`, and then call `.predict()` or `.score()`.

## Samples, features, and targets

Each row in `X` is one sample, such as one participant. Each column is a feature used
to describe that sample. `y` contains the target value the model should learn to
predict, with one target aligned to each row in `X`.

```text
X.shape → samples × features
y.shape → samples
```

```python
features = ["mean_rt", "accuracy", "age"]
X = analysis[features]
y = analysis["group"]
```

## Split before fitting

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

## Fit, predict, evaluate

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
```

Read the API:

- `LogisticRegression(...)` creates an object.
- `.fit(...)` is a method that learns from training data.
- `.predict(...)` is a method that returns predictions.
- `.coef_` is an attribute created during fitting.

## Pipelines prevent leakage

```{admonition} Common mistake
:class: dropdown warning
Calling `fit_transform()` on the complete dataset before splitting lets test rows
influence learned preprocessing values. Split first, then fit the pipeline on the
training rows only.
```

Preprocessing steps learn from data too. For example, `StandardScaler` calculates a
mean and standard deviation for every feature. If it sees the full dataset before the
train/test split, information from the test rows has already influenced the training
process. This is **data leakage**: the evaluation is no longer based on completely
unseen data.

A pipeline keeps the operations together. When the pipeline is fitted on `X_train`,
the scaler estimates its parameters from `X_train` only and passes the transformed
values to the classifier. Calling `.predict(X_test)` then applies those stored training
parameters to the test rows.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000),
)

model.fit(X_train, y_train)
```

The scaler is fitted only using training data.

```{figure} ../_static/cartoons/xkcd-machine-learning.png
:alt: A machine-learning system is drawn as a pile of linear algebra into which data is poured, with answers emerging from the other side.
:width: 620px
:align: center

The interface may be short, but the fitted model still needs to be tested and interpreted. [“Machine Learning” by Randall Munroe](https://xkcd.com/1838/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

::::{exercise} Leakage check
:label: leakage
What is wrong with scaling the complete dataset before `train_test_split`?
::::

::::{admonition} Hint
:class: dropdown
Ask which rows contribute to the means and standard deviations learned by the scaler.
Should test rows influence any quantity used during training?
::::

::::{solution} leakage
Information from the test set influences the scaling parameters. The test set is no longer fully unseen. Put scaling inside a pipeline fitted on training data.
::::

## Reproducibility

Use explicit random seeds when randomness is part of the computation:

```python
rng = np.random.default_rng(42)
train_test_split(..., random_state=42)
```

A seed does not make a flawed analysis valid; it makes the same analysis repeatable.

```{figure} ../_static/cartoons/xkcd-extrapolating.png
:alt: A line fitted through two observations is extended far beyond the observed data and used to make an absurd prediction.
:width: 520px
:align: center

A model can behave sensibly on held-out observations from the same setting and still fail when asked to predict far beyond them. [“Extrapolating” by Randall Munroe](https://xkcd.com/605/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```
