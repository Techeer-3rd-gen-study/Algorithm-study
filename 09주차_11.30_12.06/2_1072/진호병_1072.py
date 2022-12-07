import sys

input = sys.stdin.readline

def binary_search(start, end):
    mid = (start + end) // 2
    if  start > end:
        return mid
    else :
        if (Y+mid) * 100 // (X+mid) <= Z : 
            newStart = mid + 1
            return binary_search(newStart, end) 
        else :
            newEnd = mid - 1
            return binary_search(start, newEnd)



X, Y = map(int, input().split()) # X = 게임 횟수 , Y = 이긴 게임 
Z = (Y * 100) // X # Z = 승률 
if Z >= 99 :
    print(-1)
else : 
    print(binary_search(1, 1000000000) + 1) # 답은 재귀문 한번 더 돌리기전이 정답임



