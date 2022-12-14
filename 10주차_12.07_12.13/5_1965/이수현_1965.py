# 1965 : 상자 넣기

n = int(input())
box = list(map(int, input().split()))

# dp 테이블 1로 초기화
d = [1] * 1001

for i in range(1, n):
    for j in range(i):
        # 현재 위치에서 앞에 더 작은 상자가 있을 시
        if box[j] < box[i]:
            d[i] = max(d[i], d[j] + 1)
            
print(max(d))