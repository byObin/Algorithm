T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    nums = list(map(int, input().split()))
    for n in nums:
        if n % 2 == 1:
            sum += n
    print('#' + str(test_case), str(sum))