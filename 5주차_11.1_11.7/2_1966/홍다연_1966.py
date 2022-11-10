# 백준 1966 : 프린터 큐
# 처음에 m에 인덱스를 어떻게 붙여줘야 하나 고민하다, 리스트에서 pop을 할때마다 
# m의 숫자를 같이 바꿔주는 방법을 생각해보았습니다. 

test = int(input())

for _ in range(test) :
    n, m = map(int,input().split())          # 문서 개수, 문서 위치
    queue = list(map(int, input().split()))  # 문서 중요도 입력받기 
    count = 0

    while (m > - 1):
        if queue[0] == max(queue) :   # 큐의 맨 앞이 가장 크면 삭제하고, 한 칸 앞으로 보내기 
            queue.pop(0)
            m -= 1
            count += 1
        else : 
            queue.append(queue[0])   # 뒤에 추가해주고, 맨 앞 지워주기 
            queue.pop(0)

            if m == 0 :              # m = 0 이면, m이 뒤에 가게 되서, 순서 맨뒤로 변경 
                m = len(queue) - 1
            else:                    
                m -= 1

    print(count)