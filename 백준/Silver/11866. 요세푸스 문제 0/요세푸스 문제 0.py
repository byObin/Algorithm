import sys

n, k = map(int, sys.stdin.readline().split())

queue = [i for i in range(1,n+1)]
answer = []
ptr = 0

while queue:
    ptr += k-1
    if ptr >= len(queue):
        ptr %= len(queue)
    answer.append(str(queue.pop(ptr)))

print("<", ", ".join(answer), ">", sep="")