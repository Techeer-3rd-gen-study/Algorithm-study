# input : 알파벳 소문자 단어 (word)
# '우영우'같은 단어 -> 팰린드롬 맞으면 1 아니면 0


word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)


# word = str(input())

# if word[::-1] == word:
#     print(1)
# else:
#     print(0)