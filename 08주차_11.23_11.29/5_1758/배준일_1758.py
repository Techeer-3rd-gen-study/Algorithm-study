# 알바생 강호

N = int(input())
lst = [int(input()) for _ in range(N)]
rank = 1 # 등수
result = 0

lst.sort(reverse=True) # 내림차순 정렬

for tip in lst:
    tip = tip - (rank - 1)
    
    if tip >= 0: # 양수일 때 팁 받기
        result += tip
    else: # 음수면 팁 못받는다.
        break
    
    rank += 1

print(result)