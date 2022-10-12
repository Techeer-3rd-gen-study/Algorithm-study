# 문자열 반복

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄바꿈