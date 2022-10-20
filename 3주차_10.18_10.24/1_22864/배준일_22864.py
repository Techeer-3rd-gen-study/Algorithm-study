# 피로도

# A 1시간 피로도, B 1시간 일처리, C 시간당 줄어드는 피로도, M 피로도 최대치

A, B, C, M = map(int, input().split())
P, hour, work = 0, 0, 0 # 피로도, 하루, 일

while hour != 24:
    hour += 1
    
    if P + A <= M: # 일
        P += A
        work += B
        
    else: # 휴식
        if P > M: # 번아웃
            work = 0
            break
        else: # 휴식
            P -= C
            if P < 0:
                P = 0
print(work)