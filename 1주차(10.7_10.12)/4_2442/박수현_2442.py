def starPrint(star):
    for i in range(1, star):
        if i%2 == 0:
            continue
        for k in range(0, int((star-i)/2)):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        print()

if __name__ == "__main__":
    star = int(input())
    starPrint(star*2)

# 풀고 나서 다른 곳 찾아보니 파이썬이라 이렇게도 풀더군요 하하하하ㅏ
# 
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i) + "*" * (2*i-1))
