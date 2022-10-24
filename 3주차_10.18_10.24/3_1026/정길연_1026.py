N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
# b는 재배열이 안되므로, max값을 pop

ans = 0

for i in range(N) :
    max_b_idx = b.index(max(b))
    ans += a[i] * b[max_b_idx]
    b.pop(max_b_idx)

print(ans)

# list.pop(i) 인덱스 접근 유의