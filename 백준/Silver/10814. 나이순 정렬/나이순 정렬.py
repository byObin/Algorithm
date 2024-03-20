import sys

members = []

n = int(sys.stdin.readline())

for i in range(n):
    age, name = sys.stdin.readline().split()
    members.append((i, int(age), name))

sorted_mem = sorted(members, key=lambda x: (x[1], x[0]))

for j in sorted_mem:
    print(j[1], j[2])