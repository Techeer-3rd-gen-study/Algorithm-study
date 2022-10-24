# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

num = int(input())

list_a = list(input().split(" "))
list_a = map(int, list_a)
list_a = list(map(int, list_a))

list_b = list(input().split(" "))
list_b = map(int, list_b)
list_b = list(map(int, list_b))

list_a.sort(reverse=True)
list_b.sort()

s = 0
for i in range(0, num):
  s += list_a[i] * list_b[i]

print(s)
