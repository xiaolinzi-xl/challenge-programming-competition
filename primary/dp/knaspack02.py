# 完全背包问题 （物体可以使用多次）


def knaspack(w_list, v_list, w_max):
    n = len(w_list)
    dp = [[0] * (w_max + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w_max + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w_list[i - 1]:
                dp[i][j] = max(dp[i][j],
                               dp[i][j - w_list[i - 1]] + v_list[i - 1])
    return dp[n][w_max]


# 优化存储空间
def knaspack_1(w_list, v_list, w_max):
    n = len(w_list)
    dp = [0] * (w_max + 1)
    for i in range(1, n + 1):
        for j in range(w_list[i - 1], w_max + 1):
            dp[j] = max(dp[j], dp[j - w_list[i - 1]] + v_list[i - 1])
    return dp[w_max]


if __name__ == "__main__":
    w = [3, 4, 2]
    v = [4, 5, 3]
    w_max = 7
    print(knaspack(w, v, w_max))
    print(knaspack_1(w, v, w_max))
