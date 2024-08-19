import sys
input = sys.stdin.readline

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def pre_order(node):
    print(node.item, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.item, end='')


# inputs 배열에 입력 받기
n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())

# inputs 배열의 입력값들을 Node로 만들어 tree 딕셔너리 생성
tree = {}
for i, l, r in inputs:
    tree[i] = Node(i, l, r)

# 탐색 및 결과 출력
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])