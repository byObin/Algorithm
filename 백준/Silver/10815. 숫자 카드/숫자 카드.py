n = int(input())
dic = dict()
num_cards = list(map(int, input().split()))
for i in num_cards:
    dic[i] = 0
    
m = int(input())
have_cards = list(map(int, input().split()))
result = []

for j in have_cards:
    if dic.get(j) == 0:
        result.append(1)
    else:
        result.append(0)

print(' '.join(str(i) for i in result))