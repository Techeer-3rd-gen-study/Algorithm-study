# 소수찾기
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EC%99%84%EC%A0%84-%ED%83%90%EC%83%89-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

from itertools import permutations

def prime_number(n):
    if n < 2:
        return False
    
    # 약수개수 찾을 때 절반까지만 탐색해도 되므로 '// 2' 사용
    for i in range(2, n // 2 + 1):
        # 나누어 떨어지는 수가 있다면 소수 아님
        if n % i == 0:
            return False
        
    return True    

def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers) + 1):
        # 순열로 모든 경우의 수 구하기
        p.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in p]
    
    for i in set(result):
        if prime_number(i):
            answer += 1
            
    return answer