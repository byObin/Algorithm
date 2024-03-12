import sys

n = int(sys.stdin.readline().strip())

words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

words_set = set(words)	# set으로 중복 단어 하나만 남기기
words = list(words_set)	# 정렬 위해 set->list

words.sort()            # 사전순 정렬
words.sort(key = len)   # 단어길이로 정렬

for i in words:
    print(i)