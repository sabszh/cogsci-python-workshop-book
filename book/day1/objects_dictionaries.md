# Objects, methods, attributes, and dictionaries

Most scientific Python APIs become easier once you can read this pattern:

```python
result = object.method(arguments)
value = object.attribute
```

## Learn from `Path`

```python
from pathlib import Path

path = Path("data/trials.csv")

type(path)      # class of the object
path.name       # attribute
path.exists()   # method call
```

Parentheses matter: `path.exists` refers to the method itself; `path.exists()` calls it.

<div class="live-python">
  <p><strong>Check with Python:</strong> compare an attribute, a method object, and the result of calling the method.</p>
  <textarea aria-label="Editable object method and attribute example">text = &quot;  Cognitive Science  &quot;
print(&quot;attribute:&quot;, text.__class__.__name__)
print(&quot;method object:&quot;, text.strip)
print(&quot;method result:&quot;, text.strip())</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## The same pattern appears everywhere

```python
epochs.mean(axis=0)
frame.groupby("participant")
model.fit(X, y)
model.predict(X_new)
model.coef_
```

Scientific libraries create objects for recordings, tables, models, and figures. Learn
to recognise these objects and inspect the operations they provide.

```python
type(model)
dir(model)
help(model.fit)
```

## Dictionaries for research metadata

A dictionary stores named pieces of information together. This makes it useful for
metadata: an ID, condition, age, and file locations can travel as one clearly labelled
record. Nested dictionaries group related information such as the files for one
participant.

```python
participant = {
    "id": "P07",
    "condition": "control",
    "age": 24,
    "files": {
        "epochs": "P07_epochs.npy",
        "trials": "P07_trials.csv",
    },
}
```

Access and update values:

```python
participant["condition"]
participant["files"]["epochs"]
participant.get("handedness", "unknown")
participant["excluded"] = False
```

<div class="live-python">
  <p><strong>Check with Python:</strong> add another metadata field or inspect a missing key.</p>
  <textarea aria-label="Editable dictionary example">participant = {
    &quot;id&quot;: &quot;P07&quot;,
    &quot;condition&quot;: &quot;control&quot;,
    &quot;scores&quot;: [7, 9, 8],
}
participant[&quot;scores&quot;].append(10)
print(participant)
print(participant.get(&quot;handedness&quot;, &quot;unknown&quot;))</textarea>
  <button type="button">Run Python</button>
  <pre aria-live="polite">Output will appear here.</pre>
</div>

## Mutable nested objects

::::{exercise} One object or two?
:label: dict-copy
Predict the result.

```python
original = {"channels": ["Fz", "Cz"]}
copied = original.copy()
copied["channels"].append("Pz")

print(original)
```
::::

::::{admonition} Hint
:class: dropdown
`.copy()` creates a new outer dictionary. Ask whether it also creates a new list for
the value stored under `"channels"`.
::::

::::{solution} dict-copy
The outer dictionary is copied, but the nested list is shared. The result is `{'channels': ['Fz', 'Cz', 'Pz']}`. Use `copy.deepcopy` when independent nested objects are required.
::::

## Small class-reading exercise

::::{exercise} Read an object-oriented API
:label: class-reading
For each expression, identify the object, method, argument, or attribute:

```python
fig, ax = plt.subplots()
ax.plot(times, signal, label="condition A")
ax.set_title("Evoked response")
```

Then explain why `ax.plot` and `ax.plot(...)` are not the same value.
::::

::::{admonition} Hint
:class: dropdown
Read each expression from left to right: object, dot, attribute name. Parentheses turn
a method attribute into a call and may contain positional and keyword arguments.
::::

::::{solution} class-reading
- `fig` and `ax` are objects returned by `plt.subplots()`.
- `ax.plot(...)` calls the `plot` method on `ax`.
- `times` and `signal` are positional arguments; `label="condition A"` is a keyword argument.
- `ax.set_title(...)` calls another method, with the title string as its argument.
- `ax.plot` refers to the method object itself; parentheses call it and return the plotted line objects.
::::
