#!/usr/bin/python3
"""
    this script returns perimeter of grid with :
        grid is a list of list of integers:
            0 represents a water zone
            1 represents a land zone
            One cell is a square with side length 1
            Grid cells are connected horizontally/vertically (not diagonally).
            Grid is rectangular, width and height don’t exceed 100
            Grid is completely surrounded by water, and there is one island
            (or nothing).
            The island doesn’t have “lakes” (water inside that isn’t connected
            to the water around the island).
"""


def island_perimeter(grid):
    """
        calculates the perimeters
    """
    perimeter_grid = 0
    grid_size = len(grid)
    row_size = len(grid[grid_size - 1])

    for i in range(grid_size):
        for j in range(row_size):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0 and j - 1 >= 0:
                    perimeter_grid += 1
                elif j - 1 < 0:
                    perimeter_grid += 1
                if j + 1 < row_size and grid[i][j + 1] == 0:
                    perimeter_grid += 1
                elif j + 1 >= row_size:
                    perimeter_grid += 1
                if grid[i - 1][j] == 0 and i - 1 >= 0:
                    perimeter_grid += 1
                elif i - 1 < 0:
                    perimeter_grid += 1
                if i + 1 < grid_size and grid[i + 1][j] == 0:
                    perimeter_grid = perimeter_grid + 1
                elif i + 1 >= grid_size:
                    perimeter_grid += 1

    return perimeter_grid
