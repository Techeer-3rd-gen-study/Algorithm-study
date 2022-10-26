# 백준 22864번 : 피로도
# 알고리즘으로 풀이 

# 1시간 일 ⇒ 피로도 : A , 일한 양 : B , 1시간 휴식  ⇒ 피로도 : - C , 하루 피로도 MAX = M
A,B,C,M = map(int,input().split())

if A > M :   # 피로도 최대치가 더 커서 하루 1시간도 일을 못할 경우 ! 
    print (0)
else : 
    work, fatigue, hour = 0, 0, 0

    while hour < 24 : 
        if (M - fatigue) >= A :  # 한시간 이상의 피로 여유분이 있으면 일하기 
            work += B 
            fatigue += A   
        else :
            fatigue -= C   # 피로회복 
            if fatigue < 0 :
                fatigue = 0 
        hour += 1

    print(work)
