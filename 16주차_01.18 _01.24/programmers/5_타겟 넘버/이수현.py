# 타겟 넘버
# https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-DFS-BFS-Python

def solution(numbers, target):
    answer = 0
    result = [0]
    for num in numbers:
        temp = []
        for i in result:
            temp.append(i + num)
            temp.append(i - num)
        result = temp
    for i in result:
        if i == target:
            answer += 1
    return answer