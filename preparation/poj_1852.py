if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        pole, _ = map(int, input().split())
        ants = map(int, input().split())
        res_min, res_max = 0, 0
        for ele in ants:
            res_min = max(res_min, min(ele, pole - ele))
            res_max = max(res_max, max(ele, pole - ele))
        print(f'{res_min} {res_max}')
