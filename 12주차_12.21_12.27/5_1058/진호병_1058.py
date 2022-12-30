import sys
input = sys.stdin.readline
n = int(input())
s = []
visit = [[0] * n for i in range(n)]
def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if s[i][j] == "Y" or (s[i][k] == "Y" and s[k][j] == "Y"):
                    visit[i][j] = 1
for i in range(n):
    s.append(list(input().strip()))
floyd()
result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visit[i][j] == 1:
            cnt += 1
    result = max(result, cnt)
print(result)