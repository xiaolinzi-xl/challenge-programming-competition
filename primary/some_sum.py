def dfs(arr, index, sum, k):
    if index >= len(arr):
        return sum == k
    if dfs(arr, index + 1, sum, k) or dfs(arr, index + 1, sum + arr[index], k):
        return True
    return False


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if dfs(arr, 0, 0, k):
        print('Yes')
    else:
        print('No')
