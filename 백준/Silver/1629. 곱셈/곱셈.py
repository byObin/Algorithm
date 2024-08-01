# 분할 정복(DAC)로 거듭제곱 계산하는 함수
def dac(base, ex, mod):
# base : 밑, ex : 지수, mod : 나누는 수

    if ex == 0:
        return 1
    elif ex == 1:
        return base % mod
    
    # 분할 : 지수를 절반으로 나누기
    half_ex = dac(base, ex//2, mod)
    half_ex = (half_ex * half_ex) % mod

    # 지수가 홀수인 경우 추가 계산
    if ex % 2 == 0:
        return half_ex
    else:
        return (half_ex * base) % mod

a, b, c = list(map(int, input().split()))
print(dac(a, b, c))