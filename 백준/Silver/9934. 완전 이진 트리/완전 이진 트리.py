k = int(input())
bin_tree = list(map(int, input().split()))
tree = [[] for _ in range(k)]

# 현재 트리와 레벨 전달
def makeTree(arr, x):
    mid = len(arr)//2
    tree[x].append(arr[mid])
    
    if len(arr) == 1:
        return
    
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

def main():
    makeTree(bin_tree, 0)

    for i in range(k):
        print(*tree[i])

if __name__=='__main__':
    main()