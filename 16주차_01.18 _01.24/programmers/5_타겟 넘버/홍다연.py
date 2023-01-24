# 타겟 넘버

def solution(numbers, target):
    
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)

    while queue:
        temp, num = queue.pop()
        num += 1
        if num < n:
            queue.append([temp+numbers[num], num])
            queue.append([temp-numbers[num], num])
        else:
            if temp == target:
                answer += 1

    return answer