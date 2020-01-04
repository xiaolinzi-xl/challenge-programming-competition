# 01 背包问题


def dfs(idx, w_list, v_list, w_max):
    if w_max <= 0:
        return 0
    if idx >= len(w_list):
        return 0
    res = dfs(idx + 1, w_list, v_list, w_max)
    if w_max >= w_list[idx]:
        res = max(
            res,
            dfs(idx + 1, w_list, v_list, w_max - w_list[idx]) + v_list[idx])
    return res


# dp[i][j] = dp[i-1][j] j < w[i]
#         = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]) j >= w[i]
def knaspack(w_list, v_list, w_max):
    n = len(w_list)
    dp = [[0] * (w_max + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w_max + 1):
            dp[i][j] = dp[i - 1][j]
            if w_list[i - 1] <= j:
                dp[i][j] = max(dp[i][j],
                               dp[i - 1][j - w_list[i - 1]] + v_list[i - 1])

    return dp[n][w_max]


# 优化存储空间 从 O(nW) ---> O(W)
def knaspack_1(w_list, v_list, w_max):
    n = len(w_list)
    dp = [0] * (w_max + 1)
    for i in range(1, n + 1):
        for j in range(w_max, w_list[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - w_list[i - 1]] + v_list[i - 1])
    return dp[w_max]


if __name__ == "__main__":
    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    w_max = 5
    print(dfs(0, w, v, w_max))
    print(knaspack(w, v, w_max))
    print(knaspack_1(w, v, w_max))
