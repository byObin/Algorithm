# n 이하의 소수 나열하기

count = 0       # 나눗셈 한 횟수
ptr = 0         # 이미 찾은 소수의 개수

n = int(input('n을 입력하세요 : '))

prime = [None]*(n//2)   # 찾은 소수 저장하는 배열
prime[ptr] = 2          # 2는 반드시 가장 작은 소수이므로 초깃값 지정
ptr += 1

prime[ptr] = 3
ptr += 1

for i in range(5, n+1, 2):    # 2의 배수는 소수가 아니므로 홀수만 탐색
    n = 1
    while prime[n] * prime[n] <= i:
        count += 2
        if i % prime[n] == 0:   # 나누어 떨어지면 소수 아님
            break
        n += 1
    else:               # 끝까지 나누어 떨어지지 않으면 소수임
        prime[ptr] = i  # 소수이므로 prime배열에 입력
        ptr += 1
        count += 1

for i in range(ptr):
    print(prime[i])

print(f'나눗셈 한 횟수 : {count}')