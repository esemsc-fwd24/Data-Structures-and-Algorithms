# First create helper functions and dictionaries
# from stack import Stack

offsets = {"up": (0, 1), "right": (1, 0), "down": (0, -1), "left": (-1, 0)}


def is_legal_pos(maze, pos):
    """
    A function to determine if the current position is on the board or is an obstacle

    Inputs
    ------
    maze: 2D list of the maze in total
    pos: tuple indicating the (i ,j) position of the cell being checked

    Outputs
    ------
    Returned: Bool, True if cell is within the bounds of the board and False if not

    """
    i_max, j_max = len(maze) - 1, len(maze[0]) - 1
    i, j = pos[0], pos[1]

    if 0 > i or i > i_max or 0 > j or j > j_max:
        return False
    elif maze[i][j] == "*":
        return False
    else:
        return True


def get_path(predecessors, start, goal):
    """
    A function to return the path of the list of predecessors after the game has finished.
    Predecessors is a dictionary with the key as the start cell up to the penultimate cell.

    Inputs
    ------
    predecessors: dictionary

    start: tuple, coordinates of the first cell

    goal: tuple, coordinates of the goal cell

    Output
    ------
    list of tuples, containing the list of coordinates of the path from beginning to end
    """
    current_cell = goal
    path = []
    while current_cell != start:
        path.append(current_cell)
        current_cell = predecessors[current_cell]
    path.append(start)
    path.reverse()
    return path


def maze_game(maze, start, goal):
    # Initialise the stack
    stack = Stack()

    # Initialise the predecessors dictionary
    predecessors = {start: None}

    # Push the start cell to the top of the stack
    stack.push(start)

    # Iterate through until the stack is empty
    # ( the condition for if we have reached goal
    # is elsewhere to account for the case if the goal
    # isn't reached).

    while not stack.is_empty():
        current_cell = stack.pop()

        if current_cell == goal:
            # Return the path
            return get_path(predecessors, start, goal)
        else:
            # Iterate through each direction and add to stack if
            # legal
            for direction in ["up", "right", "down", "left"]:
                row_move, col_move = offsets[direction], offsets[direction]
                neighbour = (
                    current_cell[0] + row_move,
                    current_cell[1] + col_move,
                )
                if is_legal_pos(maze, neighbour):
                    stack.push(neighbour)
                    predecessors[neighbour] = current_cell
    return None


predecessors = {
    (0, 0): None,
    (0, 1): (0, 0),
    (1, 0): (0, 1),
    (1, 1): (1, 0),
    (2, 0): (1, 1),
    (3, 0): (2, 0),
    (3, 1): (3, 0),
    (3, 2): (3, 1),
    (3, 3): (3, 2),
}


maze = [
    ["", "", "*", ""],
    ["", "", "*", ""],
    ["", "*", "*", ""],
    ["", "", "", "O"],
]
