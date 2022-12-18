# T28 - MINESWEEPER.PY

import random # Used to generate random grid dimension between 4 and 10
import math # Used for rounding in determining maximum number of mines to assign

def generate_minesweeper_grid():
    grid_dimension = random.randint(3,10) # Generate a random grid dimension between 3 and 10
    maximum_mines_per_row = math.ceil(grid_dimension/3) # Determines maximum number of mines per row by capping at 1/3 of grid dimension
    starting_grid = [] # Empty grid initialisation
    mine_count = 0 # Used in below for loop for allocation of mines

    # Produces a grid of mined and mine-free elements by random generation based on user-defined dimension
    for j in range(0, grid_dimension):
        row_template = [] # Resets at start of each row to produce a uniquely mined row
        for i in range(0, grid_dimension):
            is_mine_randomizer = random.randint(0,1) # Random binary variable to decide if element is mined or not
            # Ensures maximum number of mines per row is not exceeded to ensure a fairly even distribution
            if is_mine_randomizer == 0 or mine_count == maximum_mines_per_row: 
                row_template.append("-")
            elif is_mine_randomizer == 1 and mine_count < maximum_mines_per_row:
                row_template.append("#")
        starting_grid.append(row_template)

    # Print output of the grid view to the user
    print(f"\nGame grid of {grid_dimension}x{grid_dimension} cells randomly generated and successfully mined:\n")
    for i in starting_grid:
        print(*i, sep = " | ")

    # Loop through all cells in the starting grid and check surrounding cells, count mines and replace '-' with number of mines
    for i, sublist in enumerate(starting_grid):
        for j, element in enumerate(sublist):
            count_mines = 0
            # Skip the mined cells
            if starting_grid[i][j] == '#':
                continue
            # Rotate around the surrounding cells
            for row_pan in range(-1, 2):
                if (i + row_pan) < 0 or (i + row_pan) >= grid_dimension: # Skip if the row to check is out of range
                    continue
                for col_pan in range(-1, 2):
                    if (j + col_pan) < 0 or (j + col_pan) >= grid_dimension: # Skip if the col to check is out of range
                        continue
                    if starting_grid[i + row_pan][j + col_pan] == '#': # If a specific cell is a mine, increase mine count
                        count_mines += 1
            starting_grid[i][j] = count_mines # Overwrite dash with the total mine once surrounding mines have been checked

    # Print the newly formatted game grid showing the number of mines surrounding each cell to the user
    print("\nMinesweeper game grid has been formatted below:\n")
    for i in starting_grid:
        print(*i, sep = " | ")

# Defines length of border printed before each section, for UI and readability purposes
border_length = 65 
print('─'*border_length, "\nMINESWEEPER GAME")

generate_minesweeper_grid()
