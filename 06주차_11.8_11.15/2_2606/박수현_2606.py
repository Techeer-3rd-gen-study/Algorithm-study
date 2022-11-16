import sys

input = sys.stdin.readline
cnt = 0
def dfs(node):
    global cnt
    check[node] = 1
    
    for i in graph[node]:
        if check[i] == 0:
            dfs(i)
            cnt += 1

computer_num = int(input())
connected_computer_num = int(input())

graph = [[] for _ in range(computer_num+1)]
for _ in range(1, connected_computer_num+1):
    computer_index, computer_value = map(int, input().split(" "))
    graph[computer_index].append(computer_value)
    graph[computer_value].append(computer_index)

check = [0]*(computer_num+1)
dfs(1)
print(cnt)
