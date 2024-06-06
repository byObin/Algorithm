word = input()
part_str = set()

for start in range(len(word)):
    for end in range(start+1, len(word)+1):
        part_str.add(word[start:end])

print(len(part_str))