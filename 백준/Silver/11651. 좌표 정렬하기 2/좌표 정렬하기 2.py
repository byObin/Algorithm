n = int(input())

pairs = []

for _ in range(0,n):
    x, y = map(int, input().split())
    pairs.append((y,x))

pairs.sort()

for i in range(0,n):
    print(pairs[i][1],pairs[i][0])
