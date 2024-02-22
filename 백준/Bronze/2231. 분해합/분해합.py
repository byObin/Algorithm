n = int(input())
exist = False

def sum_of_each_numbers(num):
    numbers = []
    while num >= 1:
        numbers.append(num%10)
        num  = num // 10
    return sum(numbers)

for i in range(1,n+1):
    if sum_of_each_numbers(i)+i == n:
        print(i)
        exist = True
        break

if exist == False:
    print(0)