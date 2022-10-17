# 10988 펠린드롬인지 확인하기 

word = input()

backward = ''.join(reversed(word))

if word == backward : 
    print(1)
else :
    print(0)

