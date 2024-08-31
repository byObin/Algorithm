n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr2 = [0] * 2000000
for i in range(n):
    arr2[arr[i]] = i

cnt = 0
for i in range(n):
    if arr2[x - arr[i]] > i:
        cnt += 1

print(cnt)