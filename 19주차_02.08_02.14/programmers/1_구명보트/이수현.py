# 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        # 최솟값 + 최댓값이 제한보다 작거나 같은 지 확인
        if people[0] + people[-1] <= limit:
            answer += 1
            # 둘다 큐에서 제거
            people.pop()
            people.popleft()
        # 최솟값보다 크면 무거운 사람만 제거
        else:
            answer += 1
            people.popleft()
    # 큐에 1명만 남았을 경우
    if people:
        answer += 1
    return answer