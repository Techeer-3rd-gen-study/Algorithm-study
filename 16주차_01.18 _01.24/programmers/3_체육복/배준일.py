def solution(n, lost, reserve):
    # 전체 학생 수, 도난당한 학생 번호 배열, 여벌 체육복 가져온 학생 번호 배열
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당했을 경우
    # 리스트로 하면 에러나서 set으로 차집합 연산 
    set_reserve = set(reserve) - set(lost) 
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1) # set의 remove는 O(1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
            
    return n - len(set_lost) # 전체 길이 - 도난 당한 학생 수
