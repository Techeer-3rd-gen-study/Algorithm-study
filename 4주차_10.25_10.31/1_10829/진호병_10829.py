N = int(input())

binaryArr = [] # 이진수 저장할 배열

while N != 0: # 이진수 구할때까지 반복
    binaryArr.append(N % 2) # 2로 나눴을 때 나머지 값 배열에 저장
    N = N // 2 # 그 다음 계산할 몫

binaryArr.reverse() # 거꾸로 들어가서 reverse

result = ''.join(map(str, binaryArr)) # 리스트 to 문자열

print(result)
