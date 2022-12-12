# 14494번 다이나믹이 뭐에요?

n, m = map(int,input().split())

d = [ [0] * (m + 1) for _ in range(n + 1) ]
d[1][1] = 1    # 시작 

for x in range(1, n + 1):
    for y in range(1, m + 1):
        if x == 1 and y == 1 :
            continue
        
        # 좌표값 = 옆 + 아래 + 오른쪽 아래 
        d[x][y] = d[x - 1][y] + d[x][y - 1] + d[x - 1][y - 1]

print( d[n][m] % 1000000007 )
