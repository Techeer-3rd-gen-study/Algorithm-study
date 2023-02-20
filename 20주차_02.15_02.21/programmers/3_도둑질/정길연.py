def solution(money):
    answer = 0
    
    # 원형이므로, 첫 집과 마지막집이 둘 다 선택되면 안됨 
    # 케이스를 3개로 나눠서 진행 
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    dp3 = [0] * len(money)
    
    # 마지막 집이 무조건 들어갈 때 (0번째 집은 포함안됨)
    dp1[0] = 0
    dp1[1] = money[1]
    
    for i in range(2, len(money)):
        dp1[i] = max(money[i]+dp1[i-2], dp1[i-1])
    result1 = dp1[len(money)-1]
    
    
    # 0번째 집이 들어갈 때 (마지막집은 들어가면 안됨)
    dp2[0] = money[0]
    dp2[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1): 
        dp2[i] = max(money[i]+dp2[i-2], dp2[i-1])
    result2 = dp2[len(money)-2]
    
    # 둘다 안들어갈 때
    dp3[0] = 0
    dp3[1] = money[1]
    
    for i in range(2, len(money)-1): 
        dp3[i] = max(money[i]+dp3[i-2], dp3[i-1])
    result3 = dp3[len(money)-2]
    
    
    answer = max(result1, result2, result3)
    
    return answer