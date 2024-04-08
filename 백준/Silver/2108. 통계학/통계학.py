import sys
from collections import Counter

# input()으로 입력 받으면 시간초과 발생
input = sys.stdin.readline  
n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

mean = round(sum(nums) / n) # 1. 산술평균(소수점 이하 첫째 자리에서 반올림한 값 출력)

median = nums[n // 2]       # 2. 중앙값

# 3.최빈값
freq = Counter(nums)
most_com = freq.most_common()
max_freq = most_com[0][1]

modes = [val for val, freq in most_com if freq == max_freq]

mode = modes[0] if len(modes) == 1 else modes[1]

range_val = nums[-1] - nums[0]  # 4. 범위

print(mean)
print(median)
print(mode)
print(range_val)