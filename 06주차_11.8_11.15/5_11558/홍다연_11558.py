# 백준 11558번 : The game of death

# 예제가 너무 이해하기 어려워서 구글링 하면서 이해했던것 같아요.

def dfs(num):
    for i in graph[num]:
        # 현재 친구와 연결된 친구를 재귀적 방문 
        if picked[i] == 0:
            picked[i] = picked[num] + 1  # 경로 길이 +1 
            dfs(i)
            

t = int(input())      # 테스트 케이스 수 (= 게임 횟수로 이해했습니다)
for _ in range(t):   
    n = int(input())  # 플레이어 수 
    graph = [[] for _ in range(n+1)]

    # 1번 플레이어 부터 지명 
    for i in range(1, n+1):  
        v = int(input())
        graph[i].append(v)


    picked = [0] * (n+1)  # 플레이어까지 최단 경로 길이 

    dfs(1)    # 1번 희현이 시작 

    if picked[n] > 0 :    # 주경이가 지목된 횟수가 1회 이상일 경우 
        print(picked[n])
    else :
        print(0) 