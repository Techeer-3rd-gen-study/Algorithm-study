def solution(people, limit):
    answer = 0
    people.sort()
    # i = 0
    s = 0
    e = len(people)-1
    
    # while True:
        # if i == len(people)-2:
        #     sum_pep = people[i] + people[i+1]
        #     if sum_pep > limit:
        #         answer += 2
        #         break
        # sum_pep = people[i] + people[i+1]
        # if sum_pep <= limit:
        #     answer += 1
        #     i += 2
        # else:
        #     answer += 1
        #     i += 1
    pair = 0
    while s < e :
        if people[s] + people[e] <= limit :
            s += 1
            pair += 1
        e -= 1

    answer = len(people) - pair
    
    return answer