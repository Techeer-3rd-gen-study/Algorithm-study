n, diff = map(int, input().split())

sequence = [int(input()) for _ in range(n)]
sequence.sort()

left, right = 0, 0
result = int(2e9)

while left < n and right < n:
    if sequence[right] - sequence[left] < diff:
        right += 1
    elif sequence[right] - sequence[left] >= diff:
        result = min(result, sequence[right] - sequence[left])
        left += 1

print(result)