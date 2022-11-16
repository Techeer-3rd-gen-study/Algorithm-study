# 14248 : 점프점프

import sys
input = sys.stdin.readline

n = int(input().rstrip())
visted = [0] * (n+1)
bridge = list(map(int, input().rstrip().split()))
s = int(input().rstrip())

# 출발점도 방문한 돌이므로 1부터 세기
count = 1

def dfs(x):
    # 함수 밖에서 정의한 count를 사용하기 위해
    global count

    for i in range(2):
        # 오른쪽 이동
        if i == 0:
            nx = x + bridge[x]
        # 왼쪽이동
        else:
            nx = x - bridge[x]
        # 방문하지 않은 돌 방문
        if 0 <= nx < n and not visted[nx]:
            visted[nx] = 1
            count += 1
            dfs(nx)

dfs(s - 1)
print(count)
