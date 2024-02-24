n = int(input())
count = 0
i = 0

while count <= n:
    if '666' in str(i):
        count += 1
        if count == n:
            print(i)
            break
    i += 1