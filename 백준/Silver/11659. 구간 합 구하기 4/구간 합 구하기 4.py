import sys
input = sys.stdin.read
data = input().split()

n, m = map(int, data[0:2])
nums = list(map(int, data[2:n+2]))

sums = [0] * (n+1)
for i in range(1, n+1):
    sums[i] = sums[i-1] + nums[i-1]

def get_sum(a, b):
    return sums[b] - sums[a-1]

index = n+2
results = []
for _ in range(m):
    a, b = map(int, data[index:index+2])
    index += 2
    results.append(get_sum(a, b))

print("\n".join(map(str, results)))