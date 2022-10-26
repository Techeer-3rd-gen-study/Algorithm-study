num = int(input())

list_a = list(input().split(" "))
list_a = map(int, list_a)
list_a = list(map(int, list_a))

list_a.sort()
sum = 0
wait_time = 0

for i in range(0, num+1):
  wait_time = 0
  for j in range(0, i):
    wait_time += list_a[j]
  sum += wait_time

print(sum)
