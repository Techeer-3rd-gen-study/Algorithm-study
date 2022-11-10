# 국회의원 선거

N = int(input()) # 후보의 수
giho = [int(input()) for _ in range(N)] 
buying = 0 # 매수

while True:
    if N == 1: # 다솜이 혼자만 나왔을 때
        break
    elif max(giho[1:]) < giho[0]: # 다솜이를 제외한 최대값 < 다솜이
        break
    elif max(giho) == giho[0]:
        buying += 1
        break
    else: # max(giho) != giho[0]
        buying += 1 # 매수자 +1
        max_idx = giho.index(max(giho)) # 최대값 인덱스
        giho[max_idx] -= 1 # 최대값 -1
        giho[0] += 1 # 다솜이 +1

print(buying)