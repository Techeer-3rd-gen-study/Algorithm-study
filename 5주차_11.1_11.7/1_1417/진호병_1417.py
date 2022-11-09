N = int(input())

NPeople = [int(input()) for _ in range(N)] # 배열로 받은 투표 수 저장

if N > 1: # N이 두개 보다 적으면 계산 필요 x 
    remainMax = max([NPeople[i] for i in range(1,N)]) # 다솜이를 제외한 나머지 투표 수의 최대값을 구함
    count = 0 

    while NPeople[0] <= remainMax : # 위에서 구한 최대값이 다솜이보다 크면 매수를 더 해야한다는 의미 
        remainMaxIndex = NPeople.index(remainMax,1,N) # 인덱스 1 부터 찾기 시작 // 다솜 제외 최대값 인덱스 찾기 
        NPeople[remainMaxIndex] -= 1 # 그 인덱스 값에 해당하는 값을 -1 
        NPeople[0] += 1 # 그리고 다솜이 +1 
        remainMax = max([NPeople[i] for i in range(1,N)]) # 수정된 배열에서 다시 최대값 검사 
        count += 1


    print(count)

else : 
    print(0)








