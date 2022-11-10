# 로봇 시뮬레이션
# 참고 링크 : https://mungto.tistory.com/258

direction_num = {'N': 0, 'E': 1, 'S': 2, 'W':3, 0:'N', 1:'E', 2:'S', 3:'W'}
# 문제를 기준으로 동서남북 이동시 필요한 y,x를 적어준다.
direction_to_position = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W':(0, -1)}


def find_direction(start, command, repeat):
    # 회전횟수는 4번 마다 원위치이므로 모듈연산
    repeat %= 4 
    # 시작번호를 받아와서
    start_num = direction_num[start]
    # 방향에 맞춰 돌려본다.
    if command == 'L':
        start_num-=repeat
        # 0보다 적어지면 보정
        if start_num < 0: start_num += 4
    # 반대도 마찬가지
    else:
        start_num+=repeat
        if start_num > 3: start_num -= 4
    return direction_num[start_num]


answer = None
A, B = map(int, input().split())
field = [[0 for _ in range(A)] for _ in range(B)]
# 0번 인덱스는 쓰지않을것이기 때문에 임시번호를 넣어준다.
robots = [0]
N,M = map(int, input().split())
for i in range(N):
    # 입력이 y,x가 아니라 x,y로 들어온다 주의
    x, y, direction = input().split()
    # 그림은 1번부터 쓰는데 인덱스는 0번부터 시작해서 보정해준다.
    x, y = int(x)-1, int(y)
    # 그림은 밑에서부터 시작하니까 y축을 뒤집어서 위치를 보정해준다.
    robots.append([B-y, x, direction])
    field[B-y][x] = i+1
# 위의 작업이 끝나면 예시와 같은 모양이 나오게 된다.

for i in range(M):
    # 로봇번호, 명령어, 횟수
    idx, command, repeat = input().split()
    idx, repeat = int(idx), int(repeat)
    y, x, direction = robots[idx]
    # 전진일때 처리
    if command == 'F':
        # 이동위치에 필요한 값을 받는다.
        dy, dx = direction_to_position[direction]
        # 이동해야 하는 횟수만큼 반복한다.
        for i in range(repeat):
            # 이동할 좌표를 계산하고
            move_y, move_x = y+dy, x+dx
            # 맵밖으로 벗어나지 않았다면 동작
            if 0 <= move_y < B and 0 <= move_x < A:
                # 이동하는 위치에 로봇이 있다면 충돌처리
                if field[move_y][move_x]:
                    answer = 'Robot {} crashes into robot {}'.format(idx, field[move_y][move_x])
                    break
                # 이동이 가능하고 이동할 위치에 아무것도 없다면
                else:
                    # 현재위치에 정보를 없애고
                    field[y][x]=0
                    # 이동위치에 로봇정보를 표시하고
                    field[move_y][move_x] = idx
                    # 현재 정보를 이동한 위치정보로 갱신해준다.
                    y, x = move_y, move_x
                    # 로봇의 정보또한 마찬가지로 갱신해준다.
                    robots[idx] = [move_y, move_x, direction]
            # 맵 밖으로 나갔다면 밖으로 나갔다고 정답 갱신하기
            else:
                answer = 'Robot {} crashes into the wall'.format(idx)
                break
    # 회전일때 처리
    else:
        # 현재보는 방향과 명령과 횟수를 전달하여 정보갱신
        robots[idx][2] = find_direction(direction, command, repeat)
    # 정답이 생겼다면 충돌이 생긴것이다.
    if answer: break

# 정답이 비어있다면 통과로 변경해주기
if not answer: answer = 'OK'
print(answer)