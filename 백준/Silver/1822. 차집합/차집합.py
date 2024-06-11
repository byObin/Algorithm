na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a - b

print(len(result))
if len(result) > 0:
    print(' '.join(str(i) for i in sorted(result)))