# 홍다연_예제4_2 : 시각

# 시간 입력받기 
hour = int(input())

count = 0

for h in range(hour+1) :
    for m in range(60): #분
        for s in range(60): #초
            if '3' in (str(h) + str(m) + str(s)) : 
                count += 1

print(count)
