# 팰린드롬인지 확인하기

word = list(input())
if word == word[::-1]: # 현재 단어와 뒤집은 단어가 같으면 펠린드롬
    print('1')
else:
    print('0')
