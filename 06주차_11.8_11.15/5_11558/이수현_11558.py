# 11558 : the game of death

def dfs(v):
    for i in people[v]:
        # 탐색하지 않은 노드 dfs 탐색
        if check[i] == 0:
            check[i] = check[v] + 1
            dfs(i)

t = int(input())

for _ in range(t):
    # 희현이가 지목한 주경
    point = int(input())
    people = [[] for _ in range(point + 1)]
    check = [0] * (point + 1)

    # 희현이 제외하고 플레이어가 지목한 사람 입력받기
    for i in range(1, point + 1):
        people[i].append(int(input()))

    dfs(1)

    # 주경이를 걸리게 할 수 있다면
    if check[point] > 0:
        print(check[point])
    else:
        print(0)