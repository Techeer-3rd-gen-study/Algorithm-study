# 20291번 : 파일 정리

n = int(input())

dic = {} 

for _ in range(n):
    file = input().split(".")[1]
    
    if file in dic: 
        dic[file] += 1 
    else: 
        dic[file] = 1

result = sorted(dic.items())

for i in range(len(result)):
    print(result[i][0], result[i][1])