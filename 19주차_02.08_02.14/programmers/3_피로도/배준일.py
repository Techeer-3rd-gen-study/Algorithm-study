# 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    for permu in permutations(dungeons, len_dungeons):  # 순열로 모든 경우 만들기 // 예시 : [80, 20], [50, 40], [30, 10]
        temp_k = k  # k는 그대로 보존하기 위해 temp_k를 k로 초기화 하고 사용
        count = 0  # 던전 수
        for p in permu: # 예시 : [80, 20]
            if temp_k >= p[0]:  # 최소 필요 피로도가 체크
                temp_k -= p[1]  # 소모 피로도 빼주기
                count += 1  # 던전 수 +1
        answer = max(answer, count)  # 최대 던전 수 추출
    return answer

solution(80, [[80, 20], [50, 40], [30, 10]])