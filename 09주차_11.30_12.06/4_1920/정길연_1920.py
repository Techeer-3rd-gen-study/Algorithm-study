n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()   # 이분 탐색을 위해 미리 정렬

# m안에 있는 수가 n에 있는 지 확인
for i in range(m):  
    left, right = 0, n

    while True:
        mid = (left + right) // 2
        if left <= right and mid < n:  
            if n_list[mid] == m_list[i]:  
                print(1)
                break
            elif n_list[mid] < m_list[i]:     # m의 요소가 n의 요소보다 크다면 right를 줄여야하는데 인덱스가 아닌 '값'을 줄여야하므로, left 인덱스를 +1해준다
                left = mid + 1
            elif n_list[mid] > m_list[i]:
                right = mid - 1
        else:
            print(0)
            break
            

    
