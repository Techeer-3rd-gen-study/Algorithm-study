# 20920번 : 영단어 암기는 괴로워 (https://www.acmicpc.net/problem/20920)

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 단어 개수, 단어 길이

dic = {}

# 단어 입력받아 dic 딕셔너리에 단어, 단어 개수 추가하기 
for _ in range (n) :
    word = input().strip()

    if len(word) < m : 
        continue
    else : 
        if word in dic :
            dic[word] += 1
        else : 
            dic[word] = 1


# 빈도수 계산 -> sort(key = lambda x:(-기준1, -기준2, 기준3))
# 기준 1.자주 나오는 단어   2.단어의 길이  3.알파벳 사전순    # x[0] -> 단어, x[1] -> 단어 빈도수 
dictionary = sorted(dic.items(), key = lambda  x : (-x[1], -len(x[0]), x[0]))   

for i in dictionary:
    print(i[0])
