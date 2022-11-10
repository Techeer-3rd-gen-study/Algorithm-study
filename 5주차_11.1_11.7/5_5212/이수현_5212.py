# 지구온난화

import copy

# 50년 뒤 사라지는 섬이면 False, 살아있는 섬이면 True를 리턴
def survive_land(x, y, data_map):
    # 섬의 삼면 이상이 바다이면
    if data_map[x + 1][y] + data_map[x - 1][y] + data_map[x][y + 1] + data_map[x][y - 1] >= 3:
        return False
    else:
        return True

r, c = map(int, input().split())

# 바다 : 1, 땅 : 0
# 지도 바깥부분도 바다로 감싸기 위해 +2
# 지도를 1(바다)로 초기화
data_map = [[1] * (c+2) for i in range(r+2)]

# 땅의 위치를 저장하는 변수
land_loc = [] 

for i in range(r):
    data = input()
    # enumerate() : 인덱스와 원소를 동시에 접근 가능한 함수 
    for num, d in enumerate(data):
        # 땅이 들어오면 0으로 바꾸기
        if d != ".":
            # 바깥부분을 추가했으니 인덱스 1씩 더하기
            data_map[i + 1][num + 1] = 0
            land_loc.append([i + 1, num + 1])

# 얕은 복사를 하면 이전데이터를 변경하면 같이 변하므로 깊은 복사
new_map = copy.deepcopy(data_map)

# 50년 뒤에 땅이 남아있는 지 확인
for x, y in land_loc:
    if not survive_land(x, y, data_map):
        new_map[x][y] = 1

# 지도 크기
INF = 1e9   # 1e9 = 1*109 = 1000000000
# min, max 함수를 사용하기 위해 최솟값은 최대한 크게, 최댓값은 최대한 작게 초기화
min_x, min_y, max_x, max_y = INF, INF, -INF, -INF

# 땅인 경우만 생각해서 x, y의 최솟값, 최대값 구하기
for y, new_map_data in enumerate(new_map):
    for x in range(len(new_map_data)):
        if new_map[y][x] == 0:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# 지도 출력을 해준다.
for y in range(min_y, max_y + 1):
    for i in new_map[y][min_x : max_x + 1]:
        if i == 1:
            print(".", end="")
        else:
            print("X", end="")
    print()
    