from queue_ds.my_queue import Queue

offsets = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}


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


def bfs_maze(maze, start, goal):
    queue = Queue()
    predecessors = {start: None}
    queue.enqueue(start)

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            ni, nj = offsets[direction]
            neighbour = (current_cell[0] + ni, current_cell[1] + nj)

            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell

    return None


if __name__ == "__main__":
    s = 4
    maze = [[0] * s for row in range(4)]
    maze[0][2] = maze[2][1] = maze[2][3] = "*"
    start = (0, 0)
    goal = (3, 3)
    result = bfs_maze(maze, start, goal)
    print(result)
