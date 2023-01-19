def solution(array, commands):
    answer = [] # 계산 후 생긴 값 리턴
    
    for command in commands:
        new_array = array[command[0] - 1 : command[1]] # 주어진 범위에 맞게 자르기
        new_array = sorted(new_array) # 정렬
        answer.append(new_array[command[2] - 1]) # 결과값 answer에 추가

    return answer