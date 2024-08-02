# ProgressBar
A simple GUI-less progress bar for displaying progress in a text console. This class was adapted from the book "Python Cookbook" by David Ascher, Alex Martelli, and Anna Ravenscroft.

# Installation
You can clone the repository and import the class into your project.

```bash
git clone https://github.com/yourusername/progressbar.git
```

# Usage

## Usage from within the main script
```
python progressbar.py
```

## Using within another script
You can also use the ProgressBar class from within another script or function:

```
# another_script.py
import time
from progressbar import ProgressBar

def some_function_with_progress():
    total = 50
    pb = ProgressBar(total)
    for i in range(total + 1):
        pb.progress(i)
        time.sleep(0.2)  # Simulate work being done

if __name__ == "__main__":
    some_function_with_progress()
```
