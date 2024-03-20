# 이진 검색 알고리즘

from typing import Any, Sequence

"""시퀀스 a에서 key와 일치하는 원소 이진 검색"""
def bin_search(a: Sequence, key: Any) -> int:
    high = 0        # 검색 범위 맨 앞 원소 index
    low = len(a)-1  # 검색 범위 맨 뒤 원소 index

    while True:
        mid = (high + low) // 2  # 검색 범위 중앙 원소 index
        if a[mid] == key:
            return mid   # 검색 성공
        elif a[mid] < key:
            high = mid + 1   # 검색 범위 뒤쪽 절반으로 좁힘
        else:
            low = mid - 1    # 검색 범위 앞쪽 절반으로 좁힘
        
        if high > low:
            break   
    
    return -1   # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력 : '))
    x = [None] * num    # 원소 수가 num인 배열 생성

    print('배열 데이터를 오름차순으로 입력하세요')
    x[0] = int(input('x[0]: '))

    for i in range(1,num):
        while True:
            x[i] = int(input(f'x[{i}] : '))

            # 직전에 입력한 값 보다 큰 값을 입력해야 함
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('검색할 값을 입력하세요 : '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('찾는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')