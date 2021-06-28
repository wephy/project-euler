# Path sum: three ways

import os
import numpy as np

size = 80
matrix = np.loadtxt(os.path.join("..", "data", "p083.txt"),
                    usecols=range(size), delimiter=",", dtype=int)

# size = 5
# matrix = np.array([
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ])

nodes = [*np.ndindex((size, size))]

selected = None
unvisited = {node: 9999999 for node in nodes}

while len(unvisited.keys()) > 0:
    if selected is None:
        selected = (0, 0)
        visited = {selected: matrix[selected[0], selected[1]]}
        del unvisited[selected]
    else:
        selected = min(unvisited, key=unvisited.get)
        visited[selected] = unvisited[selected]
        del unvisited[selected]

    neighbors = []
    if selected[0] == 0:
        neighbors.append((selected[0]+1, selected[1]))
    elif selected[0] == size-1:
        neighbors.append((selected[0]-1, selected[1]))
    else:
        neighbors.append((selected[0]-1, selected[1]))
        neighbors.append((selected[0]+1, selected[1]))

    if selected[1] == 0:
        neighbors.append((selected[0], selected[1]+1))
    elif selected[1] == size-1:
        neighbors.append((selected[0], selected[1]-1))
    else:
        neighbors.append((selected[0], selected[1]-1))
        neighbors.append((selected[0], selected[1]+1))

    for neighbor in neighbors:
        new_estimate = visited[selected] + matrix[neighbor[0], neighbor[1]]
        if neighbor in visited:
            if new_estimate < visited[neighbor]:
                visited[neighbor] = new_estimate
        if neighbor in unvisited:
            if new_estimate < unvisited[neighbor]:
                unvisited[neighbor] = new_estimate
