import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
after_enter = {}

for _ in range(n):
    chat = input().rstrip()
    
    if chat == 'ENTER':
        after_enter = {}
        continue
    
    if not chat in after_enter:
        after_enter[chat] = True
        cnt += 1
print(cnt)