# 2609번 : 최대공약수와 최소공배수

## 방법1 유클리드 호제법 사용
a , b = map(int, input().split())

n , m = max(a , b), min(a , b)

while m > 0 :            # m이 0일때 종료   
    n , m = m , n % m    # m = n % m 의 나머지 값

print(n)                 # 최대 공약수
print((a * b) // n)      # 최소 공배수



## 방법2 파이썬 내장함수 사용
# import math
# a, b = map(int, input().split())
# print(math.gcd(a,b))
# print(math.lcm(a,b))