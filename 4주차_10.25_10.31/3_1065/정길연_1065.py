num = int(input())

hansu = 0

for i in range(1, num+1):
    numlist = list(map(int, str(i)))
    
    # 100보다 작을때는 무조건 해당 수 만큼 한수 취급 
    if i < 100:
        hansu += 1  
    # 등차수열 정의
    elif numlist[0]-numlist[1] == numlist[1]-numlist[2]:
        hansu += 1  
        
print(hansu)