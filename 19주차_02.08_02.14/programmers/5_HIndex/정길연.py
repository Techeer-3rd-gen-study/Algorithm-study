def solution(citations):
    citations.sort()
    total = len(citations)
    
    for i in range(total):
        if citations[i] >= total-i:
            return total-i
    
    
    return 0