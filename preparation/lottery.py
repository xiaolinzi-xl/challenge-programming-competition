def solve(n, m, arr):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if arr[a] + arr[b] + arr[c] + arr[d] == m:
                        return True
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if solve(n, m, arr):
        print('Yes')
    else:
        print('No')
