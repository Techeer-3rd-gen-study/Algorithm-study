# 1758 : 알바생 강호

n = int(input())
money = [int(input()) for _ in range(n)]

# 내림차순 정렬
money.sort(reverse = True)

# 강호가 받는 팁이 양수일때만 팁 계산
tip = [money[i] - i for i in range(n) if money[i] - i > 0]

print(sum(tip))