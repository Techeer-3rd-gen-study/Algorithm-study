# 백준 2667번 : 단지 번호 붙이기 

n = int(input())

group = []   # 단지 수 저장 리스트 
cnt = 0      # 집 개수 count 

# 2차원 리스트 맵 정보 입력 받기
graph = []
for i in range(n) :
    graph.append(list(map(int,input())))


def dfs(x,y) :
    global cnt
    # 주어진 범위 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= n :
        return False
    
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 1 :
        cnt += 1            # 집 개수 +1 
        graph[x][y] = 0    # 방문 체크 

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# 단지 하나 완성되면 count한 집 개수를 그룹 리스트에 저장하고, 초기화 
for i in range(n) :
    for j in range(n) :
        if dfs(i,j) == True : 
            group.append(cnt)
            cnt = 0 

print(len(group))
group.sort()
for i in group :
    print(i)


