import sys 

region = int(input())       # 지방 수
region_request = list(map(int, input().split()))     # 각 지방에 대한 요청
budget = int(input())  # 상한액



if sum(region_request) <= budget:   # 모든 요청을 수용해도 문제없는 경우
    print(max(region_request))
    sys.exit()

left, right = 0, max(region_request)    
while left <= right:
    result = 0
    upper_limit = (left + right) // 2   # 상한액 (=mid)
    for request in region_request:
        if request <= upper_limit:  
            result += request   # 요청액 더하기
        elif request > upper_limit:
            result += upper_limit   # 상한액 더하기

    if result > budget:     # 총액이 예산보다 크다면, 상한액 줄이기
        right = upper_limit - 1
    elif result <= budget:  # 총액이 예산보다 작을 경우, 상한선을 더 높게 잡아도됨
        left = upper_limit + 1

print(right)
    


