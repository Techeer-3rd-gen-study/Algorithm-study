a, b = map(int, input().split())

bignum = max(a,b)
# greatest common division : 최대공약수
gcd = 1
# least common multiple : lcm 최소공배수

while bignum != 0 :
    # a와 b의 공약수라면 list에 넣어주기
    if(a % bignum == 0 and b % bignum == 0):
        gcd = bignum
        break
    bignum -= 1

print(gcd)

lcm = a * b / gcd
print(lcm)
