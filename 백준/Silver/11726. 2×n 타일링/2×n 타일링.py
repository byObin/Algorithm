n = int(input())

nums = [1,1]

for i in range(2, n+1):
    nums.append(nums[i-2] + nums[i-1])

print(nums[n] % 10007)