# 백준 5212번 : 지구 온난화

r, c = map(int, input().split())  # 가로, 세로 
 
maps = [[] for _ in range(r)]
future = []

for j in range(r):   # 처음 지도 입력받기 
    tmp = list(map(str, input().split()))
    for i in range(c):
        maps[j].append(tmp[0][i])
        if tmp[0][i] == 'X':
            future.append((j, i))   # 땅 인 부분 따로 저장 

# 남, 북, 동, 서 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

convert = []

def ocean(maps, y, x):   # 잠길 부분 
    cnt = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
 
        if yy < 0 or xx < 0 or yy >= r or xx >= c:
            cnt += 1        # 영역 밖은 바다
            continue
        if maps[yy][xx] == '.':
            cnt += 1
    if cnt >= 3:
        convert.append((y, x))   
 
for futures in future:
    ocean(maps, futures[0], futures[1]) 
 
for obj in convert:   # 가로 세로 바꿔줬을떄도 똑같이 바다인 경우 찾기 -> 잠길부분 -> 제거 
    y, x = obj[0], obj[1]
    maps[y][x] = '.'
    future.remove((y,x)) 
 
minR, minC = future[0]
maxR, maxC = future[0]
 
for obj in future:  # 최대, 최소값 변경 
    y, x = obj[0], obj[1]
    if y < minR:
        minR = y
    elif y > maxR:
        maxR = y

    if x < minC:
        minC = x
    elif x > maxC:
        maxC = x
 
# 지도 출력 
for j in range(minR, maxR + 1):
    result = ''
    for i in range(minC, maxC + 1):
        result += maps[j][i]
    print(result)
