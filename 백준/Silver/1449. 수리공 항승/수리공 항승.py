n, l = map(int, input().split())

tapeCount = 0
pipe = [0]*1001

for i in map(int, input().split()):
    pipe[i] = 1

x = 0
while x<1001:
    if pipe[x]:
        tapeCount+=1
        x+=l
    else:
        x+=1

print(tapeCount)
