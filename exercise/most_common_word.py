import re
import collections


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[\W]', ' ', paragraph).lower().split() if word not in banned]

print(words)    
# ['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'it', 'was']

count = collections.Counter(words)
# Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})

print(count.most_common(1))
# [('ball', 2)]

print(count.most_common(1)[0][0])
# ball