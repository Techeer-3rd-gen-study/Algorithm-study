# 홍다연 11399 : ATM 
# ATM의 효율적인 인출을 위해 N명의 사람이 돈을 인출하는 데 걸리는 시간 P의 최소값 구하기 

# 1
# 1 + 2
# 1 + 2 + 3  => 1*3 + 2*2 + 3*1 

n = int(input())  

time = list(map(int,input().split())) 
time.sort()

sum = 0

for i in range(n) :
    sum += time[i] * (n-i) 

print(sum)
