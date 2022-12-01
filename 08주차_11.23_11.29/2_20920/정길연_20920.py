# 자주 나오는 단어일수록 앞에 배치한다. <- 개수 저장
# 해당 단어의 길이가 길수록 앞에 배치한다. <- 길이 저장
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다 

import sys      # 사용하지 않으면 런타임에러 발생
input = sys.stdin.readline

n, min_len = map(int, input().split())
dic = {}

for _ in range(n):
    word = input().strip()
    if len(word) < min_len:
        pass
    elif len(word) >= min_len:
        if dic.get(word) == None:   # 존재하지 않으면 단어,길이,단어개수 추가
            dic[word] = [word, len(word), 1]
        elif dic.get(word):   # 존재하면 단어개수 추가
            dic[word][2] += 1


# sort(key= lambda x: (-기준1, 기준2, 기준3)) 
# -(기준1) : 내림차순 정렬 
# 자주 나오는 단어 - 단어 개수 내림차순 [2]
# 단어 길이 길 수록 - 단어 길이 내림차순 [1]
# 사전순 - 단어 오름차순 [0]
results = sorted(dic.items(), key= lambda x: (-x[1][2], -x[1][1], x[1][0]))
for result in results:
    print(result[0])