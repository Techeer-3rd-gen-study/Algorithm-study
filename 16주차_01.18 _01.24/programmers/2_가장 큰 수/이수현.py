# 가장 큰 수
# https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html

def solution(numbers):
    numbers = list(map(str, numbers))
    # 3자리 수로 맞춘 후 비교, 내림 차순 정렬
    # 문자열 비교는 ASCII 값으로 치환되어 정렬
    numbers.sort(key = lambda x: x * 3, reverse=True)    
    answer = ''.join(numbers)
    # 모든 값이 0일 떄를 제거하기 위해 int로 변환 후 str로 변환
    return str(int(answer))