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
