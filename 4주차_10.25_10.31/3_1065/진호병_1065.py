N = int(input())

count = 0

# 1000까지만 있다는 문제
if N <= 99: # 99까지는 모두 한수
    print(N)
elif N == 1000 : # 네자릿수는 한개만 있어 그냥 조건문으로 출력
    print(144)
else : 
    for i in range(100 ,N+1) : # 세자릿수의 경우 ex. 1 2 3 일때 1 2 / 1 3 만 비교하면 됨
        num = list(str(i))
        if(int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])):
            count += 1 # 한수 조건에 만족하면 + 1
 
    print(99+ count) # 두자릿수 고정 수에 count 더해서 출력
