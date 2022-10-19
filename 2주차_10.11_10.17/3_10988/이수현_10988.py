# 팰린드롬인지 확인하기 : 앞으로 읽을 때와 거꾸로 읽을 때가 똑같은 단어 판별

text = input()

# 입력받은 단어 역순 정렬
re_text = text[::-1]

if text == re_text:
    print(1)
else:
    print(0)