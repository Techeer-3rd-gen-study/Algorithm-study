from collections import deque

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, tree, visited, wire])
    visited[node] = True

    while queue:
        node, tree, visited, wire = queue.popleft()
        cnt += 1

        for i in tree[node]:
            if not ((node == wire[0] and i == wire[1]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])

    return cnt


def solution(n, wires):
    answer = 1e9
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    for wire in wires:
        visited = [False] * (n + 1)
        temp = []
        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire, 0)
                temp.append(cnt)

        answer = min(answer, abs(temp[0] - temp[1]))

    return answer