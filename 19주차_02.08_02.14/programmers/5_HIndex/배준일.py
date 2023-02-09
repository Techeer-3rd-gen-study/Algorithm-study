def solution(citations):
    n = len(citations) # 발표한 논문
    citations.sort() # 오름차순 정렬
    
    for i in range(n):
        if citations[i] >= n - i: # h번 이상 인용된 논문 >= h편
            return n - i
    
    return 0