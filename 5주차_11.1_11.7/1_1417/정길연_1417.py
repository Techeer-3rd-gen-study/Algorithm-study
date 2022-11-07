import math 

vote_list = list()
cnt = 0

n = int(input())

for i in range(n):
    vote_list.append(int(input()))

target = vote_list.pop(0)
vote_list.sort(reverse=True)

if len(vote_list) == 0 :
    cnt = 0
else : 
    # 처음부터 가장 많은 득표 수을 얻었을 때 매수 불필요
    if target > vote_list[0] :
        cnt = 0
    # 본인 제외 제일 많은 득표수가 본인 득표수와 같으면 1번만 매수
    elif target == vote_list[0] :
        cnt = 1
    else : 
        while vote_list[0] >= target :
            target += 1
            vote_list[0] -= 1
            cnt += 1
            vote_list.sort(reverse=True)

print(cnt)


   
    