from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        min = i     # 정렬할 부분에서 가장 작은 원소의 인덱스
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]     # 정렬할 부분 맨 앞 원소 <-> 가장 작은 원소

if __name__ == '__main__':
    num = int(input('원소의 수 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)

    print(x)