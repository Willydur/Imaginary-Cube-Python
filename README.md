**3D Latin Square Visualization with Matplotlib**

This Python script generates and visualizes a 3D representation of a Latin square using cubes in a 3D space. It utilizes the `matplotlib` library to create a 3D plot, where each cube's position and height correspond to elements in a Latin square.

**Latin Square and Cubes**

A Latin square is an n × n array filled with n different symbols, each occurring exactly once in each row and exactly once in each column. In this script, the Latin square is generated based on a given size and then represented using cubes placed in a 3D space.

**Classes and Functions**

1. `Cube` Class:

   - Represents a cube with a given position `(x, y, z)` and side length `l`.
   - Provides methods to get the vertices, faces, and a `Poly3DCollection` object for the cube.

2. `Plotter` Class:

   - Creates a 3D plot using `matplotlib` and adds a collection of cubes to visualize the Latin square.
   - The plot's axes are labeled with 'X', 'Y', and 'Z', and cube edges are drawn with red color and opacity.

3. `CarreLatin` Class:
   - Generates a Latin square of a given size.
   - Implements methods to shuffle an array and generate the Latin square based on specific rules.

**Usage**

1. Run the script.
2. Input the desired size of the Latin square when prompted.
3. The script will generate a Latin square and visualize it using cubes in a 3D plot.

**Requirements**

- Python 3.x
- `matplotlib` library

**How to Run**

1. Make sure you have Python and the required libraries installed.
2. Save the script to a `.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the command: `python script_name.py`.

**Example Output**

The script generates a 3D plot where each cube represents an element in the Latin square. The position of the cube corresponds to its row and column in the Latin square, and the height of the cube represents the value of the Latin square element.

**Note**

This script provides a visual representation of a Latin square using cubes in 3D space. It's designed for educational purposes and demonstrates how to create 3D visualizations using `matplotlib`. Feel free to explore and modify the script for further experimentation.

_Please ensure that you have the necessary dependencies installed before running the script. You can install the required dependencies using the following command:_

```bash
pip install matplotlib
```

**Author**

William BERGUE
