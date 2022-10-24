# 처음에는 두 문자열씩 비교해야하는 줄알고 어이없었는데.. 알고보니 모든 문자열에서 빈도수 높은걸
# 알아내는 거였다 휴

# 각 자리에서 가장 많이 나온거를 리스트에 넣고, 그거와 다른 것의 개수를 카운트

N, M = map(int, input().split())

# M개씩 N줄 (꼭 M개만 입력하려고 하다가 실패함 (허무))
DNA = []
for _ in range(N):
    DNA.append(input())

cnt = 0
ans = ''

# 문자열 길이만큼
for i in range(M) :
    max_DNA = [0,0,0,0]

    # 케이스 만큼
    for j in range(N): 
        if DNA[j][i] == 'A':
            max_DNA[0] += 1
        elif DNA[j][i] == 'C':
            max_DNA[1] += 1
        elif DNA[j][i] == 'G':
            max_DNA[2] += 1
        elif DNA[j][i] == 'T':
            max_DNA[3] += 1

    max_DNA_idx = max_DNA.index(max(max_DNA))
    if max_DNA_idx == 0:
        ans += 'A'
    elif max_DNA_idx == 1:
        ans += 'C'
    elif max_DNA_idx == 2:
        ans += 'G'
    elif max_DNA_idx == 3:
        ans += 'T'

    cnt += N - max(max_DNA)

print(ans)
print(cnt)