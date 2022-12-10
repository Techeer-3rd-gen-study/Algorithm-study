import sys
input = sys.stdin.readline

# x: 게임 횟수  y: 이긴 게임 횟수
x, y = map(int, input().split())
origin_rate = y * 100 // x
    # int(y/x *100) 일 경우, 오류

# origin_rate == 99 일경우, 절대 100이 되지않는다. (예외처리 좀 더 깊게 생각해보기!)
if x == y or origin_rate == 99:
    print(-1)
    sys.exit()


# 하단의 방법은 시간초과가 남 
    # why? 숫자가 커질 수록 순차적으로 탐색을 하기때문 
    #   -> 이분 탐색을 이용해서 탐색 횟수를 줄이자
left, right = 1, x      # 시작은 1, 게임 횟수로 설정 <- 게임횟수 만큼 이길경우 승률이 오를 수 밖에 없음
while left <= right:    
    mid = (left + right) // 2
    if ((y+mid) * 100 // (x+mid)) <= origin_rate:
        left = mid + 1
    elif ((y+mid) * 100 // (x+mid))  > origin_rate:
        right = mid - 1

print(right + 1)



# 시간 초과나는 방법 (이분탐색 X)

# while True:
#     odds = int(y/x * 100)
#     if odds == origin_rate:
#         y += 1
#         x += 1
#         cnt += 1
#     elif odds != origin_rate:
#         print(cnt)
#         break