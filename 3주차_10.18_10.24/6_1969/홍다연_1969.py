# 백준 1969 : DNA
# 1) dna를 입력받고, 가로 세로를 바꿔주어 첫글자들끼리, 2번째 글자들끼리 ~ 묶어준다.
# 2) 첫번째 글자 리스트에서 가장 빈출이 높은 단어를 찾고, 그 개수를 센다 (반복)
# 3) 그 단어들로 dna를 알아내고, 개수를 구한다. 

n, m = map(int, input().split())    # dna 개수, 문자열의 길이

new = []    # 결과출력될 dna
count = 0   

dna = []
for _ in range(n):
    dna.append(list(str(input())))  # 입력받은 dna 저장 

word = list(map(list,zip(*dna)))    # 행열 전환 


for i in range(m) :     
    word[i].sort()      # 알파벳 순 정렬 
    a = max (word[i],key=word[i].count)   # 빈출 높은 단어 찾기
    new.append(a)   
  
    count += word[i].count(a)    # 빈출 개수 찾기 
    

print (''.join(new))    # 리스트 -> 문자열로 변환 
print (n * m - count)    # Hamming Distance의 합 = 전체 - 공통 알파벳 


