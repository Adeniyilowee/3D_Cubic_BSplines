# 3D_Cubic_BSplines

# Overview
An interactive Cubic Basis surfaces


# Installation

```console
git clone https://github.com/Adeniyilowee/2D-Cubic-Spline
```

1. Install the libraries and dependencies
```console
cd PySubdiv
python3 setup.py install
```

# Quick Start

```python

from main.data import file

surfaces = [
        [[[0.0, 2, 0], [3, 2, -2], [6, 2, -5], [7, 2, -8], [9, 2, -10], [15, 2, -14]],
        [[0.0, 5, 0], [3, 5, -3], [6, 5, -5], [7, 5, -9], [9, 5, -12], [15, 5, -15]],
        [[0.0, 10, 0], [3, 10, -2], [6, 10, -5], [7, 10, -8], [9, 10, -11], [15, 10, -16]],
        [[0.0, 15, -1.0], [3, 15, -4], [6, 15, -6], [7, 15, -8], [9, 15, -11.5], [15, 15, -15]],
        [[0.0, 20, 1.0], [3, 20, -2], [6, 20, -4], [7, 20, -8], [9, 20, -11], [15, 20, -16]]],

        [[[0.0, 2, 3], [3, 2, 1], [6, 2, -2], [7, 2, -5], [9, 2, -7], [15, 2, -11]],
        [[0.0, 5, 3], [3, 5, 0], [6, 5, -2], [7, 5, -6], [9, 5, -9], [15, 5, -12]],
        [[0.0, 10, 3], [3, 10, 1], [6, 10, -2], [7, 10, -5], [9, 10, -8], [15, 10, -13]],
        [[0.0, 15, 2.0], [3, 15, -1], [6, 15, -3], [7, 15, -5], [9, 15, -8.5], [15, 15, -12]],
        [[0.0, 20, 4.0], [3, 20, 1], [6, 20, -1], [7, 20, -5], [9, 20, -8], [15, 20, -13]]]
        ]


w = 1
data = file.read_data(surfaces, w)

subdivision_data = data.visualize_interactive(400, 400)

```
# Visualization
![](https://github.com/Adeniyilowee/3D_Cubic_BSplines/blob/main/media/surfaces_.gif)


# Requirements
- pyvista~=0.33.0
- QtPy~=2.0.0
- PyQt5~=5.15.6
- pyvistaqt~=0.6.0
- numba~=0.55.1
- vtk~=9.1.0
- numpy~=1.22.0
- setuptools~=57.0.0


# License
The 3D Cubic Spline is under MIT license. https://choosealicense.com/licenses/mit/


# Developers
Full stack devel