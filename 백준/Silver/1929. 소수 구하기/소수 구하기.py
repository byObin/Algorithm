def find_prime(m, n):
    if m <= 2:
        print(2)

    # 홀수 소수 찾기 위한 초기화, True = 소수 후보
    primes = [False] + [True] * ((n - 1) // 2)

    for k in range(1, int((n ** 0.5) / 2) + 1):
        if primes[k]:
            primes[2 * k * (k+1) :: k * 2 + 1] = [False] * (((n + 1) // 2 - k * k * 2) // (k * 2 + 1))

    # m 이상 n 이하 소수 출력
    for i, is_prime in enumerate(primes[m//2:], start = m//2):
        if is_prime:
            prime_num = 2*i + 1
            if prime_num >= m:
                print(prime_num)

m, n = map(int, input().split())
find_prime(m, n)