a, b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

both = len(set_a & set_b)

print(a + b - (both * 2))