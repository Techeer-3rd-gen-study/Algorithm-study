# 숫자의 표현
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CLevel-2

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer