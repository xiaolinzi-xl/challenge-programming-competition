from queue import Queue

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


class Point:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step

    def __repr__(self):
        return f'x:{self.x} y:{self.y} step:{self.step}'


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    start_point = None
    for i in range(n):
        line = input().strip()
        for j in range(len(line)):
            if line[j] == 'S':
                start_point = Point(i, j, 0)
        arr.append(line)

    visited = [[False] * m for _ in range(n)]
    maze_queue = Queue()
    maze_queue.put(start_point)
    visited[start_point.x][start_point.y] = True
    ans = -1
    while not maze_queue.empty():
        point = maze_queue.get()
        for ele in directions:
            new_x, new_y = point.x + ele[0], point.y + ele[1]
            if n > new_x >= 0 and m > new_y >= 0:
                if arr[new_x][new_y] == 'G':
                    ans = point.step + 1
                    break
                if arr[new_x][new_y] == '.' and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    maze_queue.put(Point(new_x, new_y, point.step + 1))

    print(ans)
'''
10 10

#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
'''
