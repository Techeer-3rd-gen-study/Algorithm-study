# 10829번 : 이진수 변환

n = int(input())

def binary(x):
    if x == 0:
        return 
    else:
        binary(x//2)  # 몫
        print(x%2, end='') # 나머지

binary(n)