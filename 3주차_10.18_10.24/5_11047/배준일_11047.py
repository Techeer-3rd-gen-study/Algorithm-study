# 동전

n, k = map(int,input().split()) # 첫줄 N, K
money=[int(input()) for _ in range(n)] # 동전의 가치 리스트에 저장
num = 0 # 코인의 총 개수 입력 변수

for i in range(1, n+1):
    coin = money[-i] # 큰 값이 있는 뒤의 인덱스부터 계산
    if k >= coin:
        coinum = k//coin # money[-i] 동전의 개수
        k -= coin*coinum # k에서 동전만큼의 가격을 뺌
        num += coinum # 총 동전의 개수 증가

print(num)