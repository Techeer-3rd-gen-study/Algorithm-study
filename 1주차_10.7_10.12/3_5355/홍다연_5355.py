# 5355 화성 수학

T = int(input())

for i in range(T) :
    math = list(map(str,input().split()))

    # 첫 번째 문자열을 float형식으로 result에 저장 
    res = float(math[0])
    # 수식 길이 만큼 반복 계산
    for j in range(len(math)) : 
        if math[j] == '@' :
            res *= 3
        elif math[j] == '%' :
            res += 5
        elif math[j] == '#' :
            res -= 7

    print("%0.2f" %res)
    