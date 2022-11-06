# 백준 10101번 : 삼각형 외우기

angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2]:
        print("Equilateral")

    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print("Isosceles")

    else:
        print("Scalene")
    
else:
    print("Error")