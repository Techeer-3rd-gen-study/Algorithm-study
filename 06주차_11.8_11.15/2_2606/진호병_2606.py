computer = int(input())

link = int(input())


comGraph = [[0] * (computer+1) for _ in range(computer+1)]

for i in range(link):
    n,m = map(int, input().split(" ")) # 연결된 노드 갯수만큼 돌린다 . 
    comGraph[n][m] = comGraph[m][n] = 1

cnt = 0 

def dfs(start, visited = []):
    global cnt
    visited.append(start)
    
    for y in range(computer+1): # 컴퓨터 갯수 보다 하나 더 돌려야함
        if comGraph[start][y] == 1 and y not in visited: 
            dfs(y, visited)
            cnt += 1

dfs(1)

print(cnt)

