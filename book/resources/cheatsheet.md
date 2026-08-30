# Workshop cheatsheet

## Environments

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install PACKAGE
python -m pip freeze > requirements.txt
```

## Paths

```python
from pathlib import Path

root = Path.cwd()
path = root / "data" / "trials.csv"
path.exists()
path.resolve()
list(path.parent.glob("*.csv"))
```

## Objects

```python
type(obj)
dir(obj)
help(obj.method)
obj.attribute
obj.method(argument)
```

## Dictionaries

```python
record["key"]
record.get("key", default)
record.items()
record["new_key"] = value
```

## NumPy

```python
array.shape
array.ndim
array.mean(axis=0)
array[:, 0, :]
array.mean(axis=0, keepdims=True)
np.expand_dims(array, axis=0)
```

## pandas

```python
frame.head()
frame.shape
frame.dtypes
frame.loc[frame["correct"]]
frame.groupby("participant").agg(mean_rt=("reaction_time", "mean"))
left.merge(right, on="participant", validate="many_to_one")
```

## Matplotlib

```python
fig, ax = plt.subplots()
ax.plot(x, y, label="A")
ax.set(xlabel="Time", ylabel="Amplitude", title="Result")
ax.legend()
fig.tight_layout()
```

## scikit-learn

```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = model.score(X_test, y_test)
```

## Reusable scripts

```python
from pathlib import Path

def main():
    input_path = Path("data/trials.csv")
    result = run_analysis(input_path)
    save_result(result)

if __name__ == "__main__":
    main()
```

```bash
python analyse_trials.py --help
```
