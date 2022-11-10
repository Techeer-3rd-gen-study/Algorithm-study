# 백준 2979번 : 트럭 주차 

a, b, c = map(int, input().split())  

time = [0]*100

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):            # 트럭이 주차한 시간대를 모두 저장 
        time[i] += 1              

pay = 0 

for j in range(100) :
    if time[j] == 1 :
        pay += a

    elif time[j] == 2 : 
        pay += b*2

    elif time[j] == 3 :
        pay += c*3

print(pay)
