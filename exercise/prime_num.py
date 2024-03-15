# n 이하의 소수 나열하기

count = 0
n = int(input('n을 입력하세요 : '))
for i in range(2,n+1):
    for j in range(2,i):
        count += 1 
        if i%j == 0:    # 나누어 떨어지면 소수 아님
            break
    else:               # 끝까지 나누어 떨어지면 소수임
        print(i)

print(f'나눗셈 한 횟수 : {count}')