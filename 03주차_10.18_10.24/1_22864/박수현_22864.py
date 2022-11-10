a, b, c, m = map(int, input().split())

# 24시간
# A         B         C         M
# 피로도    처리량    회복량    피로도 번아웃
# 5         3         2         10

tired = 0 # 피로도
throughput = 0 # 처리량
time = 24
while time > 0 and m >= a:
  # 한 번 반복할 때마다 시간 감소
  time -= 1
  # 쉴 때
  if tired + a > m:
    if tired - c < 0:
      tired = 0
    else:
      tired -= c
    continue
  # 일 할 때
  tired += a
  throughput += b
  

print(throughput)
