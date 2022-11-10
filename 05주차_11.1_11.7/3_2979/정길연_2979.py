a, b, c = map(int, input().split())

money = 0 
time = [0] * 101

# 해당 시간에 time[i] 값 +1, 마지막에 time[i] * a ``

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        time[j] += 1
    
for i in range(1, 101):
    if time[i] == 0:
        pass
    if time[i] == 1 :
        money += a
    elif time[i] == 2 :
        money += 2 * b
    elif time[i] == 3 :
        money += 3 * c

print(money)
