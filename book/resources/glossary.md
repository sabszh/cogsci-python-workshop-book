# Python glossary

## Core language

**argument**  
A value supplied when calling a function: `round(3.1415, 2)` has two arguments.

**attribute**  
Information accessed on an object without calling it, such as `array.shape`.

**class**  
A definition of a kind of object and the behaviour associated with it. `Path` and `DataFrame` are classes.

**dictionary**  
A mutable collection mapping unique keys to values.

**function**  
A named, reusable unit of behaviour that may accept inputs and return an output.

**immutable**  
Unable to change after creation. Strings, numbers, and tuples are immutable.

**instance**  
One concrete object created from a class: `Path("data")` creates a `Path` instance.

**iterable**  
An object that can be visited one item at a time in a loop, such as a list, string, or file.

**method**  
A function accessed through an object or class, such as `text.lower()` or `model.fit()`.

**mutable**  
Able to change in place. Lists, dictionaries, NumPy arrays, and DataFrames are mutable.

**parameter**  
A name in a function definition. In `def mean(values):`, `values` is a parameter.

**return value**  
The object produced by a function call. A function without an explicit `return` returns `None`.

## Scientific Python

**array**  
A multidimensional collection of values, normally of one data type, represented by NumPy.

**axis**  
One dimension of an array. Its scientific meaning depends on the dataset.

**broadcasting**  
NumPy's rules for applying operations to arrays with compatible but different shapes.

**DataFrame**  
A labelled, two-dimensional pandas table with rows and columns.

**estimator**  
A model-like object following methods such as `.fit()` and `.predict()` or `.transform()`.

**feature**  
An input variable supplied to a model. A feature matrix is commonly named `X`.

**shape**  
A tuple describing the size of every array dimension, for example `(80, 32, 500)`.

**tensor**  
A general term for a multidimensional numeric array, particularly common in deep learning.

## Projects and reproducibility

**dependency**  
A package required by a project.

**interpreter**  
The Python program that executes code. Different environments can contain different interpreters.

**module**  
A Python file that can define functions, classes, and variables for import.

**package**  
An installable collection of Python modules.

**virtual environment**  
An isolated Python installation and package set associated with a project.

**working directory**  
The directory from which relative paths are interpreted at runtime.
