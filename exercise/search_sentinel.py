from typing import Any, Sequence
import copy

""" 시퀀스 seq에서 key와 일치하는 원소 선형 검색(보초법) """
def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)  # seq 복사
    a.append(key)           # 보초 추가

    i = 0
    while True:
        if a[i] == key:     # 검색 값 찾으면 while문 종료
            break
        i += 1
    
    return -1 if i == len(seq) else i   # 검색 성공 : 인덱스, 검색 실패 : -1 return

if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값 : '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('찾는 원소가 존재하지 않습니다')
    else:
        print(f'검색값은 x[{idx}]에 있습니다')