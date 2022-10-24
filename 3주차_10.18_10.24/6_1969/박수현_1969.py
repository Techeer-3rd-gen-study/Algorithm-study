if __name__ == '__main__':
    n, m = map(int, input().split())
    DNA = []
    for _ in range(n):
        DNA.append(input())

    cnt = 0
    result = ''
    for i in range(m):
        A = [0, 0, 0, 0]  # A, C, G, T 개수
        for j in range(n):
            if DNA[j][i] == 'A':
                A[0] += 1
            elif DNA[j][i] == 'C':
                A[1] += 1
            elif DNA[j][i] == 'G':
                A[2] += 1
            elif DNA[j][i] == 'T':
                A[3] += 1
        idx = A.index(max(A))
        if idx == 0:
            result += 'A'
        elif idx == 1:
            result += 'C'
        elif idx == 2:
            result += 'G'
        elif idx == 3:
            result += 'T'
        cnt += n - max(A)

    print(result)
    print(cnt)