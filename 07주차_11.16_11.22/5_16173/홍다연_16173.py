# 백준 16173번 : 점프왕 젤리
# DFS 풀이 

from collections import deque
import sys
input = sys.stdin.readline

def dfs(x, y, visited) :
    # 범위 설정 (조건 1번)
    if x >= n or x <= -1 or y >= n or y <= -1 :
        return 0

    if visited[x][y] == True:
        return 0

    if game[x][y] == -1 :   # 종료 위치 도착 시, 
        print('HaruHaru')
        exit()              # 함수 종료 

    visited[x][y] = True
    for i in range(2) :
        nx = x + dx[i] * game[x][y]   # 게임에 나온 숫자만큼 이동 
        ny = y + dy[i] * game[x][y]
        dfs(nx, ny, visited)
    
    return True



n = int(input())
game = []              # 게임판 
for _ in range(n):
    game.append(list(map(int, input().split())))

visited = [ [False] * n for _ in range(n) ]   # 방문 체크용 

# 오른쪽, 아래 
dx = [1, 0]
dy = [0, 1]

# 종료 위치 도착 못하면 실패 -> Hing 
if dfs(0, 0, visited) == True :    
    print('Hing')
