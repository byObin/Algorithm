name = input()

count = dict()
key = sorted(list(set(name)))
odd = []

for k in key:
    cnt = name.count(k)
    count[k] = cnt
    # 홀수 개인 알파벳 odd에 모으기
    if cnt % 2:
        odd.append(k)

# 홀수 개인 알파벳이 1개 이상일 경우 펠린드롬 불가
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    result = ''

    # 팰린드롬 절반 생성
    for k in key:       
        result += k *  (count[k] // 2)

    # 홀수 개 알파벳 존재하면 절반 끝에 추가
    if  odd:
        result += odd.pop() + result[::-1]
    else:
        result += result[::-1]

    print(result)