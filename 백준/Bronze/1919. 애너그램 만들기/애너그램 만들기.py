str1 = list(input())
str2 = list(input())

idx = 0

while idx < len(str1):
    if str1[idx] in str2:
        str2.remove(str1[idx])
        str1.remove(str1[idx])
        idx -= 1
    idx += 1

print(len(str1) + len(str2))