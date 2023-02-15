# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow                  
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            
            y = total / b
            if y >= b:                      
                if 2*y + 2*b == brown + 4:  
                    return [y,b]
            
    return answer