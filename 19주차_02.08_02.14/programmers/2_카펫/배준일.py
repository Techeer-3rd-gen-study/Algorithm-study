# 카펫

def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow + 1) :
        if yellow % i == 0 :
            # 약수 찾기
            yellow_x = int(yellow/i) 
            yellow_y = i

            if yellow_x * 2 + yellow_y * 2 + 4 == brown : # 핵심
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                
                return sorted(answer, reverse = True) # 가로 >= 세로
    return answer

solution(8, 6)