t = int(input())

for _ in range(t):
    n = int(input())
    note_one = map(int, input().split())
    
    hash_map = {num : 1 for num in note_one}
    
    m = int(input())
    note_two = map(int, input().split())
    
    for i in note_two:
        print(hash_map.get(i, 0))