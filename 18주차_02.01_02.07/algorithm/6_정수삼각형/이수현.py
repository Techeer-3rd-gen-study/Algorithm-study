# 정수 삼각형
#https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i - 1][j]
        elif j == len(d[i]) - 1: 
            d[i][j] = d[i][j] + d[i - 1][j - 1]
        else:
            d[i][j] = max(d[i - 1][j - 1],d[i - 1][j]) + d[i][j]

print(max(d[n - 1]))