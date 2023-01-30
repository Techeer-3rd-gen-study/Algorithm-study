# 프로그래머스 다음큰숫자
def solution(n):
    c = bin(n).count('1')
    
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m