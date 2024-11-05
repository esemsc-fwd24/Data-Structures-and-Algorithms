from priority_queue import PriorityQueue


def is_legal_pos(maze, pos):
    i_max, j_max = len(maze), len(maze[0])
    i, j = pos
    if i < 0 or i >= i_max or j < 0 or j >= j_max:
        return False
    elif maze[i][j] == "*":
        return False
    return True


def get_path(predecessors, start, goal):
    current_cell = goal
    path = []
    while current_cell != start:
        path.append(current_cell)
        current_cell = predecessors[current_cell]
    path.append(start)
    path.reverse()
    return path


offsets = {"up": (0, 1), "right": (1, 0), "down": (0, -1), "left": (-1, 0)}


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two paris of frid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def a_star(maze, start, goal):
    pq = PriorityQueue()

    # Add the start point to the queue with a priority of 0
    pq.put(start, 0)
    # Initialise predecessors dictionary with start: None
    predecessors = {start: None}
    # Intialise g_values dictionary with heurstic value
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            ni, nj = offsets[direction]
            neighbour = (current_cell[0] + ni, current_cell[1] + nj)

            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost = heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell

    return None


if __name__ == "__main__":
    s = 4
    maze = [[0] * s for row in range(4)]
    maze[0][2] = maze[2][1] = maze[2][3] = "*"
    start = (0, 0)
    goal = (3, 3)
    result = a_star(maze, start, goal)
    print(result)
