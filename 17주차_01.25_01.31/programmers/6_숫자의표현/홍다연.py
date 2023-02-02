# 숫자의 표현 

def solution(n):
    count = 0                      
    for i in range(1, n+1):        
        sumN = 0                     
        for j in range(i, n+1):    
            sumN += j              
            if sumN == n:          
                count += 1          
                break
            if sumN > n:           
                break
    return count