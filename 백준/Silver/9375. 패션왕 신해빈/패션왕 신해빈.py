t = int(input())

for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        name, type = map(str, input().split())
        if type in clothes.keys():
            clothes[type].append(name)
        else:
            clothes[type] = [name]
    cnt = 1

    for k in clothes:
        cnt *= len(clothes[k]) +1
    
    print(cnt - 1)