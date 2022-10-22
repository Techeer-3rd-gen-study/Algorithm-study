A, B, C, M = map(int, input().split())

currentA = 0 # 누적 피로도
totalB = 0 # 총 일한 시간 

if A > M: # 1시간 일했을 때 피로도가 최대 피로도 보다 높을때 일할 수 없음
    print(0)
else: # 그렇지 않은 경우 
    for i in range(24):  
        if currentA <= M - A:  # 피로도가 추가될만큼의 여유가 있으면
            currentA += A # 피로도 추가
            totalB += B # 일한 시간 추가
        else :  # 피로도 추가 여유가 없으면 쉬어야함
            currentA -= C # 피로도 마이너스
            if currentA < 0: # 피로도는 음수 x 
                currentA = 0

    print(totalB)