# 알파벳개수

n = input()
lst = [0]*26 # 알파벳 a~z 총 26개. [0]을 총 26개로 초기화


for i in n:
    # ord = 아스키코드를 유니코드로 변환 (a를 넣으면 97 반환)
    lst[ord(i)-97] += 1
    
for i in lst:
    print(i, end=' ')