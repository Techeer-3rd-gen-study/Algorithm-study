n = int(input())

rockleg = list(input().split(" ")) # array

startIndex = int(input()) # 3 >> -1 해서 가야함 

count = 0 

def dfs(startIdx ,visited=[]) : # dfs로 풀기 > 일단 시작 인덱스와 visited 배열을 넘겨준다 .
    global count 
    count += 1 # 방문 가능하면 dfs 로 들어오기 때문에 +1
    visited.append(startIdx) # 방문체크 
    move = int(rockleg[startIdx]) # rockleg[2] == 2  base = 2 움직일수 있는 범위 
    for _ in range(2): # 앞 또는 뒤, 두가지 방향으로 가능하다 인덱스 범위가 배열을 벗어나지않고 방문하지않았으면 
        if (0 <= (startIdx-move) < n) and startIdx-move not in visited : 
            dfs((startIdx-move), visited)

        if (0 <= (startIdx+move) < n) and startIdx+move not in visited : 
            dfs((startIdx+move), visited)
    
dfs(startIndex-1)

print(count)
    