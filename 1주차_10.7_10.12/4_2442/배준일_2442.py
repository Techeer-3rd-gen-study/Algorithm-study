# 별 찍기 - 5

n = int(input())

for i in range(1,n+1):
    # 공백은 n-i개, *은 2*i-1개 패턴반복
    print(" "*(n-i) + "*" * (2*i-1))
