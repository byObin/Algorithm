import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in nums:
    if is_prime(i):
        cnt += 1

print(cnt)