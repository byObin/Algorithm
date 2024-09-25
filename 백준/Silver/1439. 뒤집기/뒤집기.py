S = input()
cnt = [0,0]

now = S[0]
cnt[int(now)] += 1

for i in range(1, len(S)):
    if S[i] != now:
        now = S[i]
        cnt[int(now)] += 1

print(min(cnt))