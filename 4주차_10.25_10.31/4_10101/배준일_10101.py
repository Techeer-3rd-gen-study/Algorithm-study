# 삼각형 외우기

angle = [int(input()) for _ in range(3)]

if angle[0] and angle[1] and angle[2] == 60: # 세 각의 크기가 모두 60
    print('Equilateral')
    
elif sum(angle) == 180: # 세 각의 합이 180
    if angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2]: # 두 각이 같은 경우
        print('Isosceles')
    else: # 같은 각이 없는 경우
        print('Scalene')

elif sum(angle) != 180: # 세 각의 합이 180이 아닌 경우
    print('Error')