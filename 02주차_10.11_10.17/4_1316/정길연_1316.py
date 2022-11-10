# 연속한 문자가 나와야함 앞에 나온 문자가 뒤에 또 나오면 안됨
# input : n, 단어(word) n개

# 다음 문자랑 다르면 앞에 있는거~ 새롭게 저장 -> 보다는 그냥 " 전체경우 - 떨어져있는 거랑 같은거 나오는 경우 "  가 더 직관적일듯
# 바로 다음 단어랑 같으면 pass
# 바로 다음단어랑 다르면, 해당 단어가 그 뒤쪽에 있는 지 검사 

n = int(input())
result = n

for i in range(n):
    word = input()

    for j in range(len(word) - 1) :
        if word[j] == word[j + 1] : 
          pass  
        elif word[j] in word[j+1:] :
            result -= 1
            break

print(result)