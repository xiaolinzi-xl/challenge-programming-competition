# 贪心问题 区间调度问题
if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().strip().split()))
    t = list(map(int, input().strip().split()))
    arr = [(i, j) for i, j in zip(s, t)]
    arr.sort(key=lambda x: x[1])
    print(arr)
    ans = 0
    end_time = 0
    for ele in arr:
        if ele[0] > end_time:
            ans += 1
            end_time = ele[1]
    print(ans)

'''
5
1 4 2 6 8
3 7 5 9 10
'''
