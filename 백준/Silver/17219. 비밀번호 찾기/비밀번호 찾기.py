import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = dict()

for _ in range(n):
    site, pwd = map(str, input().split())
    dic[site] = pwd

for _ in range(m):
    search = input().rstrip()
    print(dic.get(search))