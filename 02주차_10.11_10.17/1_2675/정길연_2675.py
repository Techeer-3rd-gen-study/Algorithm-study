# t입력받고
# 각 문자 t번 반복한뒤 새 문자열 result생성 

t = int(input())

for i in range(t):

    r, s = input().split()
    result = ''

    for i in s:
        result += int(r) * i

    print(result)