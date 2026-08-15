# Reading Python documentation

Scientific programming involves unfamiliar objects. Expertise does not mean remembering every method; it means finding the relevant information efficiently and checking that it applies to your object.

```{figure} ../_static/cartoons/xkcd-man-page.png
:alt: A reference page points to increasingly cryptic additional reference pages.
:width: 600px
:align: center

Documentation sometimes sends you to more documentation. Start with the signature, return value, and one small example. [“Man Page” by Randall Munroe](https://xkcd.com/1692/), licensed [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/).
```

## Start with the object

When code is unclear, inspect the value you actually have:

```python
type(value)
print(value)
repr(value)
```

For scientific objects, also look for structural information:

```python
value.shape       # NumPy arrays, tensors, DataFrames
value.dtype       # NumPy arrays and tensors
value.columns     # DataFrames
value.keys()      # dictionaries and mapping-like objects
```

## Use `help`

Python can display documentation in the editor or terminal:

```python
help(str.split)
help(dict.get)
help(np.mean)
```

For a concrete object:

```python
help(epochs.mean)
```

Focus on five parts:

1. **signature:** accepted parameters and defaults;
2. **summary:** what the function promises to do;
3. **parameters:** valid types and meanings;
4. **returns:** type and shape of the result;
5. **examples/notes:** edge cases and intended usage.

## Read a function signature

Consider a simplified signature:

```python
mean(axis=None, dtype=None, out=None, keepdims=False)
```

This tells us:

- `axis` defaults to `None`, so all values are averaged;
- `keepdims` is optional and defaults to `False`;
- keyword arguments make intent visible: `mean(axis=0, keepdims=True)`;
- optional parameters should not be changed without a reason.

You can inspect signatures programmatically:

```python
from inspect import signature

signature(np.mean)
```

## Methods versus functions

These may perform a similar operation:

```python
np.mean(epochs, axis=0)   # function from the NumPy namespace
epochs.mean(axis=0)       # method belonging to the array
```

When reading documentation, verify which one you are using. Parameters and behaviour can differ across types even when method names match.

## Attributes versus method calls

```python
epochs.shape      # attribute: access stored information
epochs.mean()     # method: perform an operation
```

If you forget parentheses, Python gives you the method object rather than its result:

```python
print(epochs.mean)    # <built-in method mean ...>
print(epochs.mean())  # a number
```

## Read examples critically

Documentation examples are demonstrations, not recipes for every dataset. Before adapting one, compare:

- object type;
- array shape or DataFrame columns;
- units;
- missing-value behaviour;
- default parameter values;
- library version.

```{admonition} Version matters
:class: warning
An online example may target a different library version. Record important package versions in an environment file and prefer the current official documentation for that version.
```

## Build a minimal experiment

When a description remains abstract, create the smallest example whose answer you can verify manually:

```python
import numpy as np

small = np.array([
    [1, 2, 3],
    [10, 20, 30],
])

print(small.shape)
print(small.mean(axis=0))
print(small.mean(axis=1))
```

This is often more informative than repeatedly running a method on a large research dataset.

## Documentation workflow in VS Code

1. Hover over a function or method to view its signature and docstring.
2. Place the cursor inside a call to see parameter hints.
3. Use **Go to Definition** to find where a name comes from.
4. Run `help(object.method)` in the Python terminal.
5. Open the official API reference if details remain unclear.
6. Test the behaviour with a tiny example.
7. Return to the research data and check type, shape, and assumptions again.

## Asking a precise question

Compare these:

> My NumPy code does not work.

> `epochs` has shape `(80, 32, 500)`. I want to average trials and preserve channels × time, but `epochs.mean(axis=2)` returns `(80, 32)`. Which axis represents trials?

The second question contains the operation, current structure, expected structure, and discrepancy. That makes it much easier for a peer, teacher, or search engine to help.

::::{exercise} Documentation detective
:label: docs-detective
Use `help(sorted)` or the official Python documentation to answer:

1. Does `sorted()` modify its input?
2. What does its `key` parameter expect?
3. How would you sort records by reaction time?
::::

::::{admonition} Hint
:class: dropdown
Look at the function signature first. Identify which arguments are required, which
have defaults, and what the Returns section says about type and shape.
::::

::::{solution} docs-detective
`sorted()` returns a new list. `key` accepts a function that extracts a comparison key from each item.

```python
ordered = sorted(records, key=lambda record: record["rt"])
```
::::
