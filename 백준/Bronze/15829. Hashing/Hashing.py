l = int(input())
str = input()

def alpha_to_int(s):
    if s == 'a': return 1
    elif s == 'b' : return 2
    elif s == 'c' : return 3
    elif s == 'd' : return 4
    elif s == 'e' : return 5
    elif s == 'f' : return 6
    elif s == 'g' : return 7
    elif s == 'h' : return 8
    elif s == 'i' : return 9
    elif s == 'j' : return 10
    elif s == 'k' : return 11
    elif s == 'l' : return 12
    elif s == 'm' : return 13
    elif s == 'n' : return 14
    elif s == 'o' : return 15
    elif s == 'p' : return 16
    elif s == 'q' : return 17
    elif s == 'r' : return 18
    elif s == 's' : return 19
    elif s == 't' : return 20
    elif s == 'u' : return 21
    elif s == 'v' : return 22
    elif s == 'w' : return 23
    elif s == 'x' : return 24
    elif s == 'y' : return 25
    elif s == 'z' : return 26
    else: return 0

hash_val = 0

for i in range(len(str)):
    hash_val += alpha_to_int(str[i]) * (31**i)

print(hash_val % 1234567891)