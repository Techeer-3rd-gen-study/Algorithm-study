total = int(input())

for _ in range(total):
    docNum , whereNum = map(int, input().split()) # 4 2 
    importance = list(map(int, input().split())) # 1 2 3 4
    idx = [0 for _ in range(docNum)] # 궁금한 문서의 배열 위치를 따로 저장해서 알아보도록 만듦 
    idx[whereNum] = 1 # 0 0 1 0
    cnt = 0 
    while True: # 궁금한 문서가 pop 될때까지 무한 반복 
        if importance[0] == max(importance) : # 큰거부터 꺼내야하니 가장 큰 수면 pop해서 순서 +1을 함 
            importance.pop(0)
            result = idx.pop(0)
            cnt += 1
            if result == 1 : # 만약에 궁금했던 숫자면 몇번째로 출력됐는지 출력하고 break
                print(cnt)
                break
        else : # 가장 큰 수가 아님 , 즉 뒤로 미룸ㄴ
            importance.append(importance.pop(0))
            idx.append(idx.pop(0))