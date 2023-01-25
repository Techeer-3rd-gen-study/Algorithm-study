# k 번째 수

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 원소 자르기
        new_array = array[(i - 1) : j]
        new_array.sort()    # 정렬
        answer.append(new_array[k - 1])     # k 번째에 있는 수 추가
    return answer
