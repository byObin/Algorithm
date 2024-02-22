n = int(input())

people = []

for i in range(n):
    x, y = map(int, input().split())
    people.append((x,y))


for j in range(n):
    rank = 1
    for k in range(n):
        if people[j][0] < people[k][0]: 
            if people[j][1] < people[k][1]:
                rank += 1
    print(rank,end=' ')