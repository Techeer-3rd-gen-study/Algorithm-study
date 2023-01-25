# 체육복
# https://rain-bow.tistory.com/30

def solution(n, lost, reserve):
    # 여벌 체육복 있는 집합
    set_reverse = set(reserve) - set(lost)
    # 체육복 잃어버린 집합
    set_lost = set(lost) - set(reserve)

    for i in set_reverse:
        # 왼쪽 요소부터 탐색
        if i - 1 in  set_lost:
            set_lost.remove(i - 1)
        # 오른쪽 요소 탐색
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    answer = n - len(set_lost)
    return answer