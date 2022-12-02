# 수 찾기

N = int(input()) 
N_list = list(map(int, input().split()))
M = int(input()) 
M_list = list(map(int, input().split()))

N_list.sort() # 이분 탐색을 위한 정렬

for num in M_list:
    start, end = 0, N-1
    ans = False # 숫자가 존재하는지
    
    while start <= end:
        mid = (start + end) // 2

        if num == N_list[mid]: # 존재하는 경우
            print(1)
            ans = True
            break

        elif N_list[mid] < num: # 찾는 수가 mid보다 큰 경우
            start = mid + 1

        elif N_list[mid] > num: # 찾는 수가 mid보다 큰 경우
            end = mid - 1
    
    if ans == False: # 존재하지 않을 경우
        print(0)

