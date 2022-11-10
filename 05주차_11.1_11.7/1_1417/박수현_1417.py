import sys

input = sys.stdin.readline

num = int(input())

dasom = int(input())
candidate = []
for i in range(num - 1):
    candidate.append(int(input()))

if num == 1:
    print(0)
else:
    result = 0
    while dasom <= max(candidate):
        candidate[candidate.index(max(candidate))] -= 1
        dasom += 1
        result += 1
    print(result)
