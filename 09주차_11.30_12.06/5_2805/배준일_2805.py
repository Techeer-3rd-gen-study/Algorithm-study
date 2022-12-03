# 나무 자르기

N, M = map(int, input().split()) # 나무의 수, 상근이가 가져가는 나무 길이

N_list = list(map(int, input().split())) # 나무 리스트

start, end = 1, max(N_list)

while start <= end:
    mid = (start + end) // 2 # 나무 자르는 높이 H
    total = 0

    for wood in N_list:
        if wood >= mid: # 나무가 절단기 높이보다 클 경우
            total += wood - mid # 나무 자른 뒤 가져갈 나무 길이 저장
    
    if total < M: # 자른 나무가 M보다 작을 때
        end = mid - 1
    else: # 자른 나무가 M보다 크거나 같을 때
        start = mid + 1

print(end)
