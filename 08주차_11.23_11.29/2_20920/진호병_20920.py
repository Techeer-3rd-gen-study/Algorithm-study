import sys 

input = sys.stdin.readline

n, m = map(int, input().split())

word_note = {}

for i in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else :
        if word in word_note : 
            word_note[word] += 1
        else : 
            word_note[word] = 1

result = sorted(word_note.items(), key=lambda x:(-x[1], -len(x[0]) ,x[0]))

for k in result:
    print(k[0])