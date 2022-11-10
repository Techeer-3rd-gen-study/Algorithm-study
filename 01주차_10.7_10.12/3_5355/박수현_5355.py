def multiple_three(num):
      return num * 3

def plus_five(num):
  return num + 5

def minus_seven(num):
  return num - 7

def cal(num, sign):
  if sign == "@":
    return multiple_three(num)
  elif sign == "%":
    return plus_five(num)
  elif sign == "#":
    return minus_seven(num)

if __name__ == "__main__":
    line = int(input())
    result = []

    for x in range(0, line):
      str = input()
      list = str.split(' ')
      num = list[0]
      for i in range(1, len(list)):
        num = cal(float(num), list[i])
      result.append(num)
    
    for x in range(0, line):
      print(f'{result[x]:.2f}')
