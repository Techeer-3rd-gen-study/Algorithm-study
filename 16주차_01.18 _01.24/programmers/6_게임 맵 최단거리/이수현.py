# 게임 맵 최단거리
# https://velog.io/@minji0801/%EC%98%A4%EB%8B%B5%EB%85%B8%ED%8A%B8%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%8C%EC%9E%84-%EB%A7%B5-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC

from collections import deque

def solution(maps):
    answer = 0
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        # 큐가 빌 때까지
        while queue:
            x, y = queue.popleft()
            # 상하좌우 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵을 벗어나면 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                # 처음 지나가는 길이라면 거리 계산 후 다시 상하좌우 계산
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)
    
    if answer == 1:
        answer = -1
    else:
        answer
        
    return  answer