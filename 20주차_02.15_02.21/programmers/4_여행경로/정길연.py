from collections import defaultdict

def solution(tickets):
    
    routes = defaultdict(list)  # 인접리스트
    for key, value in tickets:
        routes[key].append(value)
    
    for route in routes:
        routes[route].sort()
    
    
    def dfs():
        stack = ["ICN"]
        path = []
        while len(stack) > 0:      # 스택이 비어있을 때 까지
            top = stack[-1]       # 맨 마지막 = 맨 위에 있는 노드
            if top not in routes or len(routes[top]) == 0:   # 특정 공항에서 출발하는 표가 없을 때 
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))    # top의 key에 해당하는 value 첫번째거 가져옴(위에서 정렬함)
        return path[::-1]
    
    answer = dfs()
    
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))