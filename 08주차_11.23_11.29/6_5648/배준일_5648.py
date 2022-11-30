# 역원소 정렬

# import sys
# input = sys.stdin.readline # 아무것도 안들어온거 체크하려면 readline 사용하면 안된다.

lst = []
flag = 0

while True:
    try:
        input_element = input()
        if input_element == None: # 아무것도 안들어왔을 때 
            # 백준 맞음 : None, -1 / vscode 맞음 백준 틀림 : input_element == ''
            break
        else:
            input_element = input_element.split()

            if not flag: # n 체크 안한 경우
                input_element = input_element[1:] # 첫번째 입력받는 원소(n)의 개수 제거
                for i in input_element:
                    i = int(i[::-1]) # 문자열 뒤집고 int로 형변환
                    lst.append(i)
                flag = 1 # n 체크
                continue

            for j in input_element:
                j = int(j[::-1]) # 문자열 뒤집고 int로 형변환
                lst.append(j)
    except:
        break

print(*sorted(lst), sep='\n') # 정렬 후 출력
