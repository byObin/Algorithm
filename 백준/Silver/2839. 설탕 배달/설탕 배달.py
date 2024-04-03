n = int(input())

# 5kg 봉지 최대 가능 수 부터 시작
for i in range(n//5, -1, -1):
    # 만약 5kg 봉지 최대 가능 수의 나머지가 3으로 나누어떨어지면
    if (n - (i * 5)) % 3 == 0:
        # 5kg 봉지 수 + 3kg 봉지 수의 합 출력
        print(i + (n - (i * 5)) // 3)
        break
# 루프를 마치고 나왔을 때 (5kg, 3kg으로 나누어떨어지지 않는 경우)
else:
    print(-1)