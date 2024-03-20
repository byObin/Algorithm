import sys

members = sys.stdin.readlines()[1:]

members.sort(key = lambda x: int(x.split()[0]))

print("".join(members)) 