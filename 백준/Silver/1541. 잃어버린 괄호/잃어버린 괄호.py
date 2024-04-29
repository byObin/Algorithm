data = input().split('-')

nums = []

for i in data:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    nums.append(sum)

answer = nums[0]

for i in nums[1:]:
    answer -= i
print(answer)