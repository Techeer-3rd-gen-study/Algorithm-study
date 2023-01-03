# 2529번 : 부등호 

import sys
input = sys.stdin.readline

k = int(input())
mark = input().split()

visited = [False] * 10
mx, mn = "", ""     # 최대값, 최솟값

def bfs(cnt, s):
    global mx,mn
    if cnt > k : 
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
    for i in range(10): 
        if visited[i] == False:
            # 문자열 존재 X, 계산 
            if cnt == 0 or compare(s[-1],str(i), mark[cnt - 1]):
                 # 방문 체크 -> 문자열 개수 추가 -> 방문 체크 해제 
                visited[i] = True 
                bfs(cnt + 1, s + str(i))  
                visited[i] = False


def compare(i, j, k):   # 부등호 계산 
    if k == ">":
        return i > j
    else:
        return i < j                

bfs(0, "")
print(mx)
print(mn)


