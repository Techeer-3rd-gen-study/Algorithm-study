# 1065번 : 한 수
# 한수 = 각 자리가 등차수열을 이루는 수 

n = int(input())
count = 0

# 100보다 작은 수 -> 한 수 
if n < 100 : 
        print (n)

# 100보다 큰 수 -> 100 ~ N 까지 등차수열 개수 + 99
else : 
    for i in range (100, n+1) :      
        num = list(map(int, str(i)))  
        if num[2] - num[1] == num[1] - num[0] :   
            count += 1

    print(count+99)

