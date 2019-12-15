directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def dfs(arr, x, y):
    arr[x][y] = '.'
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]

        if len(arr) > new_x >= 0 and len(arr[new_x]) > new_y >= 0 and arr[new_x][new_y] == 'W':
            dfs(arr, new_x, new_y)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        line = list(input().strip())
        arr.append(line)
    res = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                dfs(arr, i, j)
                res += 1
    print(res)
