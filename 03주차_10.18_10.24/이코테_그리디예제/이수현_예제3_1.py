# 예제 3-1 거스름돈

N = int(input(""))
count = 0

# 가장 큰 단위부터 확인
coin = [500, 100, 50, 10]

for i in coin:
    # 동전 개수 추가
    count = count + N // i

    # 남은 거스름돈
    N = N % i

    # 더 이상 거스를 돈이 없을 시 중지
    if N == 0:
        break
print(count)