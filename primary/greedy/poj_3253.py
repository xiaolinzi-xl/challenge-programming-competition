if __name__ == '__main__':
    n = int(input())
    L = list(map(int,input().split()))

    ans = 0
    while len(L) > 1:
        L.sort()
        tmp = L[0] + L[1]
        ans += tmp
        L[1] = tmp
        L.remove(L[0])
    print(ans)