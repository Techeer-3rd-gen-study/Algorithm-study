# 이진수 변환

N = int(input())
result = ''

while True:
    if N // 2 >= 1: # 몫이 1보다 클 때
        result += str(N % 2)
        N = N // 2
    elif N == 2: # 몫이 2일 때
        result += str(N % 2) + str(N // 2) # 2로 나눈 나머지 + 몫 더하기
        break
    elif N == 1: # 몫이 1일 때
        result += str(N % 2) # 2로 나눈 나머지 더하기
        break

result = result[::-1] # 문자열 뒤집기

print(result)