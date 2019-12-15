# 贪心算法 字典序最小问题
if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    arr = []
    left, right = 0, len(s) - 1
    while left < right:
        if ord(s[left]) < ord(s[right]):
            arr.append(s[left])
            left += 1
        elif ord(s[left]) > ord(s[right]):
            arr.append(s[right])
            right -= 1
        else:
            l, r = left, right
            while l <= r:
                if ord(s[l]) < ord(s[r]):
                    arr.append(s[left])
                    left += 1
                    break
                elif ord(s[l]) > ord(s[r]):
                    arr.append(s[right])
                    right -= 1
                    break
                else:
                    l += 1
                    r -= 1
            if l > r:
                arr.append(s[left])
                left += 1
    arr.append(s[left])
    print(''.join(arr))
