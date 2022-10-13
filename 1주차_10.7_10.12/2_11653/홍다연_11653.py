# 11653 소인수분해

num = int(input())

for i in range(2, num+1):    # 2 ~ num까지 
    if num == 1 :            # 몫이 1이면 종료 
        break;
    if num % i == 0:         # 같은 숫자를 나눌 수 있을 때까지 나누기 
        while num % i == 0:
            print(i)
            num = num / i

