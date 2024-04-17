import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pocketmon_list_id = {}
pocketmon_list_name = {}

for i in range(1, n+1):
    p = input().strip()
    pocketmon_list_id[i] = p
    pocketmon_list_name[p] = i

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(pocketmon_list_id[int(q)])
    else:
        print(pocketmon_list_name[q])
