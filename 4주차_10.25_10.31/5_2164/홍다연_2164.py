# 백준 2164번 : 카드2
# 수식으로 계산, 답 = (card - 2의제곱)*2
 
card = int(input())
a = 2                     # 2의 제곱 관리 변수 

if (card < 3) :
    print(card)

else : 
    while (a < card) :   # 뽑은 카드에 가장 가까운 2의 제곱 찾기 
        a *= 2

    ans = (card - (a//2)) * 2  # 수식 

    print(ans)
        
        

'''
## 풀이 -> 시간 초과 
card = list(range(1,int(input())+1))

while (len(card)>1) :
    card.pop(0)
    first = card.pop(0)
    card.append(first)

print(card[0])  
'''
