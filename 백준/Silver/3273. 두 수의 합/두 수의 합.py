n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 배열 정렬 후 포인터 양쪽 끝에 두 개 설정
arr.sort()
left, right = 0, n - 1
cnt = 0

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(cnt)