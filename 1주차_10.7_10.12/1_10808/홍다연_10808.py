# 10808번 알파벳 개수

word = input()
lst = [0]*26

for i in word :
    lst[ord(i)-97] += 1

for j in lst :
    print(j, end=' ')
