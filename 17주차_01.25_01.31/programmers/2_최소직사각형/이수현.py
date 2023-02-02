# 최소 직사각형

def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        # 가로와 세로 중 큰 길이를 h, 작은 길이를 w에 몰기
        if w > h:
            w, h = h, w
        max_w, max_h = max(w, max_w), max(h, max_h)
    return max_w* max_h