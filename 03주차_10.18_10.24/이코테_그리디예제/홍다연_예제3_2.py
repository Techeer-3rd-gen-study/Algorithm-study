# 홍다연_예제3_2 : 큰 수의 법칙
# 배열에서 가장 큰 수 K번 더하기 + 두번째 큰수 한번 + 가장 큰수 K번 ... 총 M 번 더하기 

# n:배열의 크기, m:숫자 더해지는 횟수, k:최대 연속 횟수 
n, m, k = map(int, input().split())

# 숫자 배열
num = list(map(int, input().split()))

num.sort(reverse=True) # 숫자 내림차순 정렬 
first = num[0]
second = num[1]

sum = 0 
while m > 0 :
    for i in range(k): # 가장 큰수 K 번 반복 
        sum += first
        m -= 1
    
    sum += second
    m -= 1

print(sum)