import sys
input = sys.stdin.readline

def dfs(num, arr):
    # 방문한 노드 -2로 표시
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
del_node = int(input())
cnt = 0

dfs(del_node, arr)
cnt = 0

for i in range(n):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)