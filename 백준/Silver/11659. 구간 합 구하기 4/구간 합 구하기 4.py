import sys
input = sys.stdin.read
data = input().split()  # 한번에 입력 받기

n, m = map(int, data[0:2]) 
nums = list(map(int, data[2:n+2]))

sums = [0] * (n+1)      # 누적합 저장할 sums 배열 초기화
for i in range(1, n+1):
    sums[i] = sums[i-1] + nums[i-1]

index = n+2
results = []
for _ in range(m):
    a = int(data[index])
    b = int(data[index + 1])
    index += 2
    results.append(sums[b] - sums[a-1])

print("\n".join(map(str, results))) # results 값들 한줄씩 출력