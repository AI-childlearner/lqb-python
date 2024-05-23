import os
import sys
import itertools

# 请在此输入您的代码
# 表示相邻元素
dict = {'a': ['f', 'b'], 'b': ['a', 'c', 'g'], 'c': ['b', 'd', 'g'],
        'd': ['e', 'c'], 'e': ['d', 'f', 'g'], 'f': ['a', 'e', 'g'],
        'g': ['b', 'c', 'e', 'f']}
s = 'abcdefg'
ans = []
cnt = 0
# 先找出全排列 在去全排列里筛选
for i in range(1, 8):
    for x in itertools.combinations(s, i):
        ans.append("".join(x))

for str1 in ans:
    if len(str1) == 1:
        cnt += 1
        continue

    for situation in itertools.permutations(str1):
        for c in range(1, len(situation)):
            if situation[c - 1] not in dict[situation[c]]:
                break

        else:
            cnt += 1
            break

print(cnt)