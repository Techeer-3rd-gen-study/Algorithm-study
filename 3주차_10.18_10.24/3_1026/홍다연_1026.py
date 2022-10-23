# 백준 1026 : 보물
# 리스트 A,B의 곱의 합을 최소로 만들기 위해 A 변경시키기 
# 배열 A 만 변경해서 문제를 해결하는 방법을 해결하지못해, 새로운 리스트로 사본을 만드는 방법 이용 

n = int(input())
a = map(int, input().split())
b = map(int, input().split())

aprime = sorted(a)                 # 작은순서대로 리스트 새로 생성
bprime = sorted(b, reverse=True)  # 큰순서대로 리스트 새로 생성 

s = 0
for i in range(n):
    s += aprime[i] * bprime[i]

print(s)