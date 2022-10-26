# 사람의수 N
# 각 사람이 걸리는 시간 P
# 각 사람이 돈을 인출하는 데 필요한 시간의 최소합 ans

# 최소 시간부터 오름차순 정렬 -> 해당 인덱스까지 더함

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)

ans = 0

for i in range(N+1) :
    ans += sum(P[0:i])

print(ans)

# sum(P[0:i])을 생각하는데 시간이 좀 걸림