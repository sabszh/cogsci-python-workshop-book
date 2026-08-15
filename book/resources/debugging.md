# Debugging research code

```{figure} ../_static/cartoons/xkcd-debugger.png
:alt: One person wonders how they can understand their brain when the brain is also the tool used for understanding.
:width: 460px
:align: center

Debugging the tool used for debugging. [“Debugger” by Randall Munroe](https://xkcd.com/1163/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

Debugging is an investigation, not a sign that you are bad at programming.

## Read tracebacks from the bottom

```text
Traceback (most recent call last):
  ...
ValueError: operands could not be broadcast together with shapes (32,500) (32,)
```

Start with:

1. Error type: `ValueError`
2. Error message: incompatible shapes
3. Your line nearest the bottom

## Inspect the smallest useful facts

```python
print(type(value))
print(array.shape)
print(frame.columns.tolist())
print(frame.dtypes)
print(path.resolve())
print(path.exists())
```

## Common error patterns

| Error | First question |
|---|---|
| `NameError` | Was the variable created in this execution? |
| `KeyError` | Which dictionary keys or DataFrame columns exist? |
| `IndexError` | What is the size of that axis? |
| `AttributeError` | What is the object's actual type? |
| `ModuleNotFoundError` | Which interpreter/environment is running? |
| broadcasting `ValueError` | What are both shapes? |
| file not found | What does the resolved path say? |

## Reduce the example

Replace a large pipeline with a tiny object that reproduces the error:

```python
small = epochs[:2, :3, :10]
print(small.shape)
```

## Ask a high-quality question

Include:

- what you expected;
- what happened;
- the complete error;
- relevant types and shapes;
- a minimal code example;
- what you already tried.
