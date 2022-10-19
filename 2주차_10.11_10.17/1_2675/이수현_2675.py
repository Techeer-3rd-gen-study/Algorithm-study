# 문자열 반복

T = int(input())

for _ in range(T):
    # 반복횟수와 문자열 나눠서 입력받기
    n, text = input().split()

    for i in range(len(text)):
        print(int(n) * text[i], end = "")
    # 새 문자열 입력받고 다음줄에서 다시 입력받기
    print()
