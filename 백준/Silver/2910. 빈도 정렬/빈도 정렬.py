n, c = map(int, input().split())
nums = list(map(int, input().split()))

dic = {}
order = 0

# dic[숫자] = [빈도, 출현순서] 형태로 저장
for i in nums:
    if i in dic:
        dic[i][0] += 1
    else:
        dic[i] = [1, order]
        order += 1
# 출현빈도(내림차순), 출현순서(오름차순) 순으로 정렬
sorted_dic = sorted(dic.items(), key = lambda x: (-x[1][0], x[1][1]))

result = []
# 출현횟수만큼 result에 추가(append 반복보다 빠름)
for num, (cnt, _) in sorted_dic:
    result.extend([num] * cnt)

# * : 리스트 요소 개별 인자로 출력
print(*result)