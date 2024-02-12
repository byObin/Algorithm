n = int(input())
sold = {}
for _ in range(n):
    title = input()
    if title in sold:
        sold[title] +=1
    else:
        sold[title] = 1

sold_list = sorted(sorted(sold.items()), key=lambda x: x[1], reverse=True) 

print(sold_list[0][0])