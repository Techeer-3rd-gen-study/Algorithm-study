n = int(input())

data = list(map(int, input().split()))

data.sort() # 정렬을 통해 최소 시간이 들 수 있도록 재배열 

def fun(total): # 각 사람마다 걸리는 시간 함수로 구현
    sum = 0
    for i in range(total+1):
        sum += data[i]
    return sum # 걸리는 시간을 리턴함(사람 당)

result = 0 # 총 소요시간 

for i in range(n):
    result += fun(i) # 총 사람들 걸리는 시간

print(result)
