t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    file = list(map(int, input().split()))

    answer = 1

    while file:
        if file[0] < max(file):
            file.append(file.pop(0))
        else:
            if m == 0:
                break
            file.pop(0)
            answer += 1

        m = m-1 if m > 0 else len(file) - 1

    print(answer)