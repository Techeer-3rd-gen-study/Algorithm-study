# 20920 : 영단어 암기는 괴로워

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
words = {}

for _ in range(n):
    word = input().rstrip()
    # 단어의 길이가 m보다 클 경우만 단어장 생성
    if len(word) >= m:
        # 단어장에 이미 있는 단어라면
        if word in words:
            words[word] += 1
        # 단어장에 없는 단어라면
        else:
            words[word] = 1

# 자주 나오는 단어, 단어의 길이, 알파벳 사전순으로 정렬
words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])