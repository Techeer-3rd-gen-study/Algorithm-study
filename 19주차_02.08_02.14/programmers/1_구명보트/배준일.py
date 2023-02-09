def solution(people, limit):
    answer = 0
    
    people.sort() # 정렬
    
    start, end = 0, len(people) - 1
    
    while start <= end:
        answer += 1 # if문 충족 여부와 상관없이 +1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    
    return answer