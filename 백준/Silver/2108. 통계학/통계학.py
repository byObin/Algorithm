import sys
from collections import Counter

input = sys.stdin.readline  
n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

mean = round(sum(nums) / n)

median = nums[n // 2]

frequencies = Counter(nums)
most_common = frequencies.most_common()
max_freq = most_common[0][1]

modes = [val for val, freq in most_common if freq == max_freq]

mode = modes[0] if len(modes) == 1 else modes[1]

range_val = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(range_val)