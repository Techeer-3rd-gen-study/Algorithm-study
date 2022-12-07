# 예제2 : 부품찾기

# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는 지 확인
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')