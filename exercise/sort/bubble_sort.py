from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        last = n-1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last

    for j in range(left, right):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            last = j
    right = last


if __name__ == '__main__':
    num = int(input('원소의 수 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort(x)

    print(x)