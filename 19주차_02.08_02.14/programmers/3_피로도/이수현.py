# 피로도

from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0
    
    for permut in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count
    
    return answer