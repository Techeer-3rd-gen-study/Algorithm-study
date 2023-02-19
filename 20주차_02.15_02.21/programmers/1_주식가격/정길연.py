from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices) 
    
    for i in range(len(queue)):
        x = queue.popleft()
        if any (x > i for i in queue):
            for i in queue:
                if x > i:
                    answer.append(queue.index(i) +1)
                    break
        else:
            answer.append(len(queue))
    
    return answer
