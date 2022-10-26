# 홍다연_예제3_3 : 숫자 카드 게임 
# 행 중에서 가장 작은 수를 고르고, 그중에서 가장 큰 수 뽑기 

row, column = map(int,input().split())
mini = []  

for i in range(row) : 
    num = list(map(int,input().split()))
    mini.append(min(num))   # 행에서 가장 작은 수 리스트에 추가 

print(max(mini))  

