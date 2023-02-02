# 다음 큰 숫자
# https://somjang.tistory.com/entry/Programmers-%EB%8B%A4%EC%9D%8C-%ED%81%B0-%EC%88%AB%EC%9E%90-Python

def solution(n):
    # bin을 이용하여 이진수로 변환한 뒤 1의 개수 세기
    one_count = bin(n).count('1')
    
    # 1의 개수가 같은 숫자 찾기
    for i in range(n + 1, 1000001):
        if one_count == bin(i).count('1'):
            answer = i
            break
    return answer