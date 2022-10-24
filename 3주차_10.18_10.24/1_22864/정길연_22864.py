a, b, c, m = map(int, input().split())
# a, b, c, m
# a : 피로도    5
# b : 일        3
# c : 쉬는 시간 2
# m : 맥스 피로도   10
# -> 가장 많은 일 (b가 최대)

# 하루는 24시간이므로 24시간에서 줄여나가면서 체크
day = 24
# 초기 피로도
st = 0
# 초기 일의 양
work = 0

if a > m :
  print(0)
else :
  while day > 0 :
    day -= 1
    # 누적 피로 + 피로 <= 맥스
    if st + a <= m :
      work += b
      st += a
    # 누적 피로 + 피로 > 맥스 -> 쉬는시간 갖기
    else :
      if st - c >= 0 :
        st -= c
        # 누적피로 - 쉬는시간 음수일 경우 0
      else :
        st = 0

  print(work)


# 대충 생각하느라 조건문 2번 빼먹어서 반성했습니다

