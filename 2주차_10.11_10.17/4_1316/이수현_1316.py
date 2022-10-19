# 그룹 단어 체커

import sys

N = int(input())

# 그룹 단어 체크 변수
group_word = 0

for _ in range(N):
    word = sys.stdin.readline()
    # 그룹 단어일 시 체크하기 위해 T/F로 확인
    check = True

    # 그룹단어 체크
    for i in range(len(word) - 1):
        # 문자열의 첫 원소와 다음 원소를 비교하여 서로 다르면
        if word[i] != word[i + 1]:

            # 이때의 원소가 뒷 원소에 있다면 확인 중지
            if word[i] in word[i + 1 : ]:
                check = False
                break

    # 이상없으면 그룹단어로 체크
    if check:
        group_word += 1

print(group_word)

