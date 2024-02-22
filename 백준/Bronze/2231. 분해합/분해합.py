n = int(input())

answer = 0

for i in range(1,n+1):
    if sum(map(int, str(i)))+i == n:
        answer = i
        break

print(answer)