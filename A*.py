
import heapq

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)


def heuristic(a, b):
    # Khoảng cách Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(start, goal):
    # Mỗi phần tử: (f, vị trí)
    open_set = [(heuristic(start, goal), start)]

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1]

        r, c = current

        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        ]

        for nr, nc in neighbors:
            # Kiểm tra biên bản đồ
            if not (0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])):
                continue

            # Không đi xuyên tường
            if grid[nr][nc] == 1:
                continue

            neighbor = (nr, nc)
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return None


path = astar(start, goal)
print(path)
