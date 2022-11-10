# 한수

import sys

n = int(sys.stdin.readline())
count = 0

for i in range(1, n + 1):
    # 입력받은 수까지의 숫자들을 리스트로 변환
    n_list = list(map(int, str(i)))
    # 1~99는 모두 한수
    if i < 100:
        count += 1
    # 100부터 999까지 등차수열인지 확인
    elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
        count += 1
        
print(count)