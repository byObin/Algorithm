n, r, c = map(int, input().split())

def recursive(n, r, c):
    if n == 0:
        return 0
    cur_cnt = 2 * (r % 2) + (c % 2)
    return cur_cnt + 4 * recursive(n-1, int(r/2), int(c/2))

print(recursive(n, r, c))