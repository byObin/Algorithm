import sys

input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
m = int(input())

dp_table = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):  
    dp_table[i][i] = 1     # 길이가 1이면 항상 펠린드롬

for i in range(1,n):
    if list_n[i-1] == list_n[i]:
        dp_table[i][i+1] = 1    # 길이가 2이면 두 요소가 같으면 펠린드롬

for cnt in range(2,n):          # 길이가 3이상이면
    for i in range(1, n-cnt+1):
        j = i + cnt
        if list_n[i-1] == list_n[j-1] and dp_table[i+1][j-1] == 1:
            dp_table[i][j] = 1    # 맨 앞뒤 값이 같고 그 사이가 펠린드롬이면 펠린드롬

for _ in range(m):
    s, e = map(int, input().split())
    print(dp_table[s][e])