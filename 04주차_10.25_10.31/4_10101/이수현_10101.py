# 삼각형 외우기

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

# 세 각이 모두 60도
if a == b == c == 60:
    print("Equilateral")
# 세 각의 합이 180도이고 서로 다른 두 각이 같을 경우
elif a + b + c == 180 and (a == b or b ==c or c == a):
    print("Isosceles")
elif a + b + c == 180:
    print("Scalene")
else:
    print("Error")