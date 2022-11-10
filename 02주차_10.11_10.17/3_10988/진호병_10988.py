word = input()

dorw = list(reversed(word))

result = ""

for i in dorw:
    result += i


if( word == result):
    print(1)
else : 
    print(0)