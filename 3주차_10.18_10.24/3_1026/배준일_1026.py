# 보물

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
S = 0

for _ in range(N):
    A_small = A.pop(A.index(min(A))) # A의 최소값
    B_big = B.pop(B.index(max(B))) # B의 최소값
    S += A_small * B_big

print(S)