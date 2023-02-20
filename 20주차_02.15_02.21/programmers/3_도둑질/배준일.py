def solution(money):
    dp1 = [0] * len(money) # 1번 집 털기
    dp2 = [0] * len(money) # 마지막 집 털기
    
    # 1번 집을 털고 마지막 집을 안 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집은 털지 못함
        # (바로 전 집까지 훔칠 수 있는 최댓값)와 (전전집까지의 훔칠 수 있는 최댓값 + 현재 집의 money)
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # 1번 집을 안 털고 마지막 집을 터는 경우
    dp1[0] = 0 # 1번 집 0으로 초기화
    for i in range(1, len(money)):
        # (바로 전 집까지 훔칠 수 있는 최댓값)와 (전전집까지의 훔칠 수 있는 최댓값 + 현재 집의 money)
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])