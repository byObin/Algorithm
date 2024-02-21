n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

if len(numbers)>1:
    if n % 2:
        print(numbers[n//2]**2)
    else:
        print(numbers[0]*numbers[-1])
else:
    print(numbers[0]**2)