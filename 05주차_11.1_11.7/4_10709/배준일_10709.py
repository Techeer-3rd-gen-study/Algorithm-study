# 기상캐스터

import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
area = [list(input().rstrip()) for _ in range(H)]

cloud_time = 1 # 처음 구름이 오는 시간
is_cloud = False # 바로 전에 구름이 있는지 체크

for i in range(H):
    for j in range(W):

        if area[i][j] == 'c': # 구름
            area[i][j] = 0
            is_cloud = True
            cloud_time = 1

        elif area[i][j] == '.' and is_cloud == False: # 바로 전에 구름이 나오지 않은 경우
            area[i][j] = -1

        elif area[i][j] == '.' and is_cloud == True: # 바로 전에 구름이 나온 경우
            area[i][j] = cloud_time
            cloud_time += 1

    cloud_time = 1
    is_cloud = False
    print(*area[i])