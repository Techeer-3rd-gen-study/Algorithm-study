# 랜선 자르기

K, N = map(int, input().split()) # 가지고 있는 랜선 수, 필요한 랜선 수

K_list = [int(input()) for _ in range(K)] # 가지고 있는 랜선 저장

start, end = 1, max(K_list)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for lan in K_list: # mid가 자르는 단위일 때 total은 자른 랜선의 개수
        total += lan // mid
    
    if total >= N: # N개보다 많이 만드는 경우
        start = mid + 1

    else: # N개보다 적게 만드는 경우
        end = mid - 1

print(end)