import sys

input = sys.stdin.readline

N,M = map(int, input().split()) # 4개 존재 7미터 필요

treeArr = list(map(int, input().split()))

start = 1
end = max(treeArr) # endpoint 가장 많이 짜를 수 있는 max 설정


answer = 0 

while start <= end:
    mid = (start + end) // 2
    needTree = 0

    for i in treeArr :  # 나무들을 현재 mid로 나눠서 몇미터 사용가능한지 계산 
        if i - mid > 0 :
            needTree += i - mid 
        if needTree > M :  # 이 코드 뺴면 시간 초과 남 
            break

    if needTree >= M : # 자른 나무 총합이 같거나 크면 조금 더 많이 잘라보기
        answer = mid
        start = mid+1
    else:
        end = mid - 1

print(answer)