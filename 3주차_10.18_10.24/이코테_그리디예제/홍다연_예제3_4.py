# 홍다연 예제3_4 : 1이 될 때 까지 
# (1) num - 1  (2) num % k  두 가지 연산을 통해 1이 될때까지 걸리는 횟수 

num, k = map(int, input().split())
count = 0

while (num > 1):   
    if (num % k == 0):  # 나머지가 0 이면 나눠주고, 
        num /= k
        count += 1

    else:               # 아니면 빼준다 
        num -= 1
        count += 1

print(count)
