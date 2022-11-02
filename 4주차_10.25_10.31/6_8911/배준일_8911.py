# 거북이

T = int(input())
testcases = [input() for _ in range(T)]

# 북 서 남 동
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for testcase in testcases:
    direction = 0 # 북: 0 서: 1 남: 2 동: 3
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    x, y = 0, 0

    for i in testcase:
        if i == "F":
            x += dx[direction]
            y += dy[direction]

        elif i == "B":
            x -= dx[direction]
            y -= dy[direction]
        
        elif i == "L":
            if direction == 3:
                # 현재 방향이 동쪽인 경우
                direction = 0
            else:
                # 왼쪽으로 방향 전환
                direction += 1

        elif i == "R":
            if direction == 0:
                # 현재 방향이 북쪽
                direction = 3
            else:
                # 오른쪽으로 방향 전환 
                direction -= 1

        # 영역 구하기 위해 x, y의 최대, 최소값 저장 
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

    # 영역 구하기
    print(abs(max_x - min_x) * abs(max_y - min_y))
