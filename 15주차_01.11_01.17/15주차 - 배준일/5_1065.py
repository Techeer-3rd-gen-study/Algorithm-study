# 한수
import sys

input = sys.stdin.readline # 시간 단축

num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수 -> 일의 자리, 십의 자리 차이만 있는 등차수열이기 때문에
        hansu += 1 

    else : # 100~999    
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : # 등차수열 확인
            hansu+=1

    # 1000은 어차피 한수 아니라 상관없다.
print(hansu)