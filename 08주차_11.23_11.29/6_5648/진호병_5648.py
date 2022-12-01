element = [] # 원소 담을 리스트 생성

firstArr = list(map(int, input().split())) # 첫 줄에 n개 주어지므로 따로 실행

n = firstArr[0] # 첫 인덱스가 N

for i in range(1,len(firstArr)): # N 제외 다른 원소들 element에 저장
    element.append(firstArr[i])

while len(element) != n: # 이후 오는 input 갯수는 미정 따라서 element의 갯수가 n과 같을때까지 반복
    node = list(map(int, input().split()))
    for i in range(len(node)):
        element.append(node[i])

for i in range(len(element)): # element 각 원소를 list로 만들고 뒤집어서 배열에 다시 저장
    convertInt = "" 
    eachElement = list(str(element[i]))
    eachElement = eachElement[::-1] # 순서 뒤집기
    for j in range(len(eachElement)):
        convertInt += eachElement[j]
    element[i] = int(convertInt)
    
element.sort()

for x in element:
    print(x)