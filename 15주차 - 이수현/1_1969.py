# DNA

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# dna 입력받기
dna = []
for _ in range(n):
    dna.append(sys.stdin.readline())

# Hamming Distance 합이 가장 작은 dna를 출력할 변수
result = ''
# Hamming Distance 합 계산하는 변수
cnt = 0

for i in range(m):
    # Hamming Distance 계산하는 변수
    count = [0] * 4

    for j in range(n):
        # A/C/G/T가 나온 횟수 체크
        if dna[j][i] == 'A':
            count[0] = count[0] + 1
        elif dna[j][i] == 'C':
            count[1] = count[1] + 1
        elif dna[j][i] == 'G':
            count[2] = count[2] + 1
        elif dna[j][i] == 'T':
            count[3] = count[3] + 1

    # 각 열에서 가장 많이 나온 인덱스 값 반환
    idx = count.index(max(count))

    # 가장 많이 나온 인덱스 값으로 Hamming Distance 합이 가장 작은 dna 생성
    if idx == 0:
        result = result + 'A'
    elif idx == 1:
        result = result + 'C'
    elif idx == 2:
        result = result + 'G'
    elif idx == 3:
        result = result + 'T'

    cnt = cnt + (n - max(count))

print(result)
print(cnt)