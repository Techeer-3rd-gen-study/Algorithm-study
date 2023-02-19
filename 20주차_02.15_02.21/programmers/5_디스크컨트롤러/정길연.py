# 소요시간이 작은것대로 정렬해줘야함 하지만 시작점을 고려해줘야함 -> 최소힙을 만들어주자 !
import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1  # 시작 시간
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:     # 시작 시간이 작은 순서대로 고려
                heapq.heappush(heap, [job[1], job[0]])    # 소요시간이 작은 순서대로 시행해야되므로 반대로 넣어줌
        
        if len(heap) > 0:       # 처리할 작업이 있는 경우
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]  # 소요시간 더해줌
            answer += now - curr[1]     # 시작시간을 빼줌으로서 
            i += 1
        else: # 처리할 작업이 없는 경우 다음 시간으로 넘어감
                now += 1
    
    
    return answer // len(jobs)

print(solution(([[0, 3], [1, 9], [2, 6]])))