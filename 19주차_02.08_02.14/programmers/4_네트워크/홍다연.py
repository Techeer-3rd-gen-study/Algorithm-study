# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for check in range(n):
        if visited[check] == False:
            DFS(n, computers, check, visited)
            answer += 1 
    return answer

def DFS(n, computers, check, visited):
    visited[check] = True
    for node in range(n):
        if node != check and computers[check][node] == 1: #연결된 컴퓨터
            if visited[node] == False:
                DFS(n, computers, node, visited)