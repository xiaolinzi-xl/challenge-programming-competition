# 贪心算法 Saruman's Army
if __name__ == '__main__':
    n = int(input().strip())
    r = int(input().strip())
    x = list(map(int, input().strip().split()))
    x.sort()  # 刚开始的坐标不一定是有序的
    left = 0
    ans = 0
    while left < n:
        l = left
        while l < n and x[l] - x[left] <= r:
            l += 1
        ans += 1
        print(f'分割点:{x[l - 1]}')
        point = l - 1
        left = l
        while left < n and x[left] - x[point] <= r:
            left += 1
    print(ans)

'''
6
10
1 7 15 20 30 50
'''
