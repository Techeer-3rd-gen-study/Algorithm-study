# 5648 : 역원소 정렬

list = []
check = 1

while True:
    try:
        element = input()
        # 입력값 없음(null)이면 중지
        if element == None:
            break
        else:
            element_split = element.split()
            # 첫번째 줄 입력만 n 제외하고 반환
            if check:
                element_split = element_split[1:]
                check = 0

            # 역순배열하고 정수형 반환
            for i in element_split:
                i = int(i[::-1])
                list.append(i)
        
    except:
        break 

print(*sorted(list), sep = '\n')