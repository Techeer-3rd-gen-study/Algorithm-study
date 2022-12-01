# 게임

X, Y = map(int, input().split()) # 게임 횟수, 이긴 게임
Z = Y * 100 // X # 승률
start, end = 1, 1000000000
ans = 0

def is_changed(mid):
    # mid를 더했을 때 승률 > 현재 승률
    return (Y + mid) * 100 // (X + mid) > Z
    
if Z >= 99: # 승률이 변하지 않는 경우 -> 99%, 100%
    print(-1)

else:
    while start <= end:
        mid = (start + end) // 2

        if not is_changed(mid):
            # mid를 더했을 때 승률 < 현재 승률
            start = mid + 1 # mid를 더해 승률을 높인다.
        else:
            # mid를 더했을 때 승률 > 현재 승률
            ans = mid # mid를 저장해두고 end를 줄였을 때 조건을 통과하지 못하면 ans가 답이 된다.
            end = mid - 1 
    
    print(ans)