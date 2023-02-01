def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        if w < h: # 가로 세로 중 더 긴 것을 h로 저장한다.
            w, h = h, w # 더 길 경우 스왑
        max_w = max(max_w, w) # 작은 것들 중 가장 큰 것 구하기
        max_h = max(max_h, h) # 큰 것들 중 가장 큰 것 구하기
    return max_w * max_h