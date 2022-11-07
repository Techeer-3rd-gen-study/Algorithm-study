# 백준 1417번 : 국회의원 선거 

n = int(input())

winner = int(input())   # 다솜

vote = [int(input()) for _ in range(n-1)]

count = 0   # 돈으로 매수 할 인원 수 

if n == 1 :      
    print (0)
else : 
    while max(vote) >= winner :  
        data = vote.index(max(vote))
        winner += 1
        vote[data] -= 1
        count += 1
    
    print(count)
