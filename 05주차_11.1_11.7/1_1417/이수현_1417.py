# 국회의원 선거

import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())
vote = [int(input()) for _ in range(N - 1)]
result = 0

# 다솜만 선거에 나온 경우에는 매수할 사람 없음
if N <= 1:
    print(0)

else:
    # 남은 후보자들 중 최댓값이 다솜의 표보다 클 경우에만 실행
    while max(vote) >= dasom:
        # 득표수가 최대인 후보자 인덱스 구하기
        max_index = vote.index(max(vote))
        # 표 매수
        dasom += 1
        vote[max_index] -= 1

        result += 1

    print(result)