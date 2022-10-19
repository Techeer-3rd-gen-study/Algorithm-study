# 그룹 단어 체커

N = int(input()) # 단어의 개수
result = N # 처음에 모든 케이스가 그룹 단어라고 가정

for i in range(N):

    word=input()

    for j in range(len(word)-1): # 인덱스는 0부터 시작하므로 -1 

        if word[j] == word[j+1]: # 문자가 연속해서 나오는 경우 그룹 단어
            pass

        elif word[j] in word[j+1:]: # 문자가 현재 인덱스+1부터 끝 안에 문자가 존재하면 그룹 단어가 아니므로 result에서 -1
            result -= 1
            break # 진행되던 for문 break, j+1 단계 진행

print(result)
