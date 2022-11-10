# 로봇 시뮬레이션

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

# 로봇 위치 저장할 리스트
brd = [[0] * A for _ in range(B)]

# 방향
NESW_dic = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

# 이동값
NESW_list = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]

robots = []
for i in range(N):
    # 현재 위치, 방향
    x, y, d = input().rstrip().split()
    # 로봇 위치 계산
    r, c = B - int(y), int(x) - 1
    # 로봇 위치와 방향 리스트에 저장
    robots.append([r, c, NESW_dic[d]])
    # 로봇 위치를 로봇의 인덱스로 저장
    brd[r][c] = i + 1

# 잘못된 명령일 지 체크하는 변수
flag = False

for i in range(M):
    # 로봇 인덱스, 명령(방향), 반복횟수
    robot, instruction, loop = input().rstrip().split()
    robot = int(robot)
    loop = int(loop)

    # 로봇 위치, 방향
    r, c, d = robots[robot - 1]

    if instruction == 'L' or instruction == 'R':
        # 움직일 방향
        new_d = (d + loop) % 4
        # 움직일 횟수가 짝수이면 'L'과 'R'방향에서는 같은 결과
        if loop % 2:
            if instruction == 'L':
                new_d = (new_d + 2) % 4

        robots[robot - 1] = [r, c, new_d]

    else:
        # 움직일 방향
        dr, dc = NESW_list[d]

        for j in range(1, loop + 1):
            # 로봇이 이동했을 때 땅 안에 있다면
            if 0 <= r + dr < B and 0 <= c + dc < A:
                # 로봇끼리 충돌할 경우
                if brd[r + dr][c + dc]:
                    flag = True
                    print(f'Robot {brd[r][c]} crashes into robot {brd[r + dr][c + dc]}')
                    break

                # 로봇끼리 충돌하지 않을 경우
                else:
                    brd[r][c] = 0
                    r, c = r + dr, c + dc
                    brd[r][c] = robot
                    robots[robot - 1] = [r, c, d]

            # 로봇이 벽과 충돌
            else:
                flag = True
                print(f'Robot {brd[r][c]} crashes into the wall')
                break

    # 잘못된 명령이면 중지
    if flag:
        break

# 이상없으면
if not flag:
    print('OK')