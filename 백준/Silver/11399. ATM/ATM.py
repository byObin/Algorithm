n = int(input())

time_per = list(map(int, input().split()))

time_per.sort()

time = 0

for i in range(len(time_per)+1):
    time += sum(time_per[0:i])

print(time)