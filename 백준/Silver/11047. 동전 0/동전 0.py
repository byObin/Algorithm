n, k = map(int, input().split())

w = [int(input()) for _ in range(n)]
w.reverse()

answer = 0

for i in w:
    answer += k//i
    k = k%i

print(answer)