n = int(input())
schedule = []

for _ in range(n):
    x, y = map(int, input().split())
    schedule.append((x, y))

# schedule을 끝나는 시간 기준으로 정렬
schedule.sort(key=lambda x:(x[1], x[0]))

last_ending_time = 0
cnt = 0

for start, end in schedule:
    # 시작 시간이 방금 회의 끝나는 시간 이후면
    if start >= last_ending_time:
        cnt += 1
        last_ending_time = end

print(cnt)