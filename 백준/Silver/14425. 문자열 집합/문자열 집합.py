import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
my_str = []
answer = 0
for _ in range(n):
    s.add(input().rstrip())
for _ in range(m):
    my_str.append(input().rstrip())

for i in my_str:
    if i in s:
        answer += 1

print(answer)