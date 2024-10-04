#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        last_row = triangle[i - 1]

        # Generate the middle values for the current row
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle
