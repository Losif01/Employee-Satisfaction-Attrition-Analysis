import streamlit
import pandas 
import seaborn
import pathlib
import numpy
import sklearn
import matplotlib as plt
import tabulate

# Print versions of all imported packages
print(f"streamlit == {streamlit.__version__}")
print(f"pandas == {pandas.__version__}")
print(f"seaborn == {seaborn.__version__}")
print(f"pathlib == {pathlib.__version__ if hasattr(pathlib, '__version__') else 'Built-in module'}")
print(f"numpy == {numpy.__version__}")
print(f"sklearn == {sklearn.__version__}")
print(f"matplotlib == {plt.__version__}")
print(f"tabulate == {tabulate.__version__}")