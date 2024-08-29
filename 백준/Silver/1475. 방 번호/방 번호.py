n = input()
num = [0] * 1000001
for i in n:
    num[int(i)] += 1

if num[6] != num[9]:
    sum = num[6]+num[9]
    num[6] = (sum-1) // 2
    num[9] = (sum+1) // 2

print(max(num))