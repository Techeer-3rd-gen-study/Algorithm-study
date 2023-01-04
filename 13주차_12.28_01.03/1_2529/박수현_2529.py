# 참고: https://velog.io/@jaenny/%EB%B0%B1%EC%A4%80-2529-%EB%B6%80%EB%93%B1%ED%98%B8-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython

def good(x, y, op) :
    if op == '<' :
        if x > y : 
            return False
    if op == '>' :
        if x < y : 
            return False
    return True

def go(index, num) :
  if index == n+1 : # 부등호가 n개 입력되니까 숫자는 n+1개 필요
    ans.append(num)
    return
  
  for i in range(10) :
    if check[i]: continue # 해당 숫자를 이미 사용했다면 pass

    if index == 0 or good(num[index-1], str(i), a[index-1]):
      check[i] = True
      go(index+1, num+str(i))
      check[i] = False

n = int(input())
a = input().split()

ans = []
check = [False]*10 # 해당 숫자를 사용했는지 안 했는지 체크

go(0, '')

ans.sort()
print(ans[-1])
print(ans[0])
