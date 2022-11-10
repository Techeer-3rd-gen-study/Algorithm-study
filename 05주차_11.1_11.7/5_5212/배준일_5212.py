# 지구 온난화

# 참고 링크 : https://velog.io/@heejun32/%EB%B0%B1%EC%A4%80-5212-Python
import sys
input = sys.stdin.readline

# 좌표 탐색
def traversal(x, y, MAP):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0  # 바다로 둘러 쌓여 있는지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= R + 1 and 0 <= ny <= C + 1 and MAP[nx][ny] == '.':
            count += 1
    return count

R, C = map(int, input().split())
MAP = [['.' for _ in range(C + 2)] for _ in range(R + 2)] # 지도와 지도 바깥부분 바다로 감싸기
coord = []  # 좌표 저장
for r in range(1, R + 1):
    temp = input().strip()
    for c in range(1, C + 1):
        MAP[r][c] = temp[c - 1]
        if temp[c - 1] == 'X': # X가 있는 좌표 저장
            coord.append([r, c])

# 50년뒤 사라지는지 검사 시작
del_coord = [] # 50년 뒤 사라지는 땅
for c in coord:
    x = c[0]
    y = c[1]
    if traversal(x, y, MAP) >= 3: # 바다에 잠기는지 확인
        del_coord.append([x, y])

# 지우기
for c in del_coord:
    x = c[0]
    y = c[1]
    MAP[x][y] = '.'

# 출력할 X, Y 시작, 종료 좌표 찾기
# X 포함하는 가장 작은 지도의 크기 구하기
start_x = C + 1
end_x = 0
start_y = R + 1
end_y = 0

for row in range(len(MAP)):
    if 'X' not in MAP[row]:
        continue
    else:
        start_y = min(start_y, row) # 'X' 포함하는 y좌표최소값 구하기
        end_y = max(end_y, row)
        for col in range(len(MAP[row])):
            if MAP[row][col] == 'X':
                start_x = min(start_x, col) # 'X' 포함하는 x좌표 최소값 구하기
                end_x = max(end_x, col)

for row in range(start_y, end_y + 1):
    for col in range(start_x, end_x + 1):
        print(MAP[row][col], end='')
    print()