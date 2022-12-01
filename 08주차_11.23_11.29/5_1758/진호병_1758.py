n = int(input())

tips = []

for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

sum = 0

for i in range(n):
    if (tips[i] - i) >= 0:
        sum += tips[i] - i

print(sum)