import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
for i in range(n):
    tree[i] = list(map(int, input().split()))

for i in range(n-1):
    tree[i+1][0] += tree[i][0] 
    tree[i+1][-1] += tree[i][-1]

for p in range(1,n):
    for q in range(1,p):
        tree[p][q] += max(tree[p-1][q-1], tree[p-1][q])

print(max(tree[n-1]))