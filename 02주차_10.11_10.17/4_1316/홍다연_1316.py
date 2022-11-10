# 1316 그룹 단어 체커

N = int(input())
count = 0  # 그룹단어 개수 확인 

for i in range(N):
    word = input()    # 입력받은 단어
    new = [word[0]]   # 중복 제거 단어 리스트 예) aabbbcccaa => abca
    
    for i in range(1, len(word)):
        if word[i] != word [i-1]:
            new.append(word[i])  # 바로 앞 단어와 다르면 리스트에 추가 

    # set(word)는 사용한 알파벳만 남겨준다. 
    # 사용한 알파벳 수 = 중복 제거 단어 => 그룹 단어 
    if len(new) == len(set(word)):
        count += 1

print(count)
        
