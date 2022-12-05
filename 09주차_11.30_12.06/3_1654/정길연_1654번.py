import sys

# had: 가지고 있는 랜선 개수,  need: 필요한 랜선 개수
had, need = list(map(int, input().split()))

lines = list()
for _ in range(had):
    lines.append(int(input()))
# [int(input()) for _ in range(had)]

# 만들 수 있는 최대 랜선 길이 구하기 
left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += (line // mid)
    if cnt < need:     # 자른 개수가 필요한거보다 작을때, right가 더 작아야함
        right = mid - 1
    elif cnt >= need:    # 자른 개수가 필요한거보다 많을 때, left가 더 커져야함
        left = mid + 1
    
print(right)



# 문제 : 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
# 문제 제대로 읽으면 아래와 같은 코드를 쓰면 안되는데,.
# if had >= need:     
#     print(min(lines))
#     sys.exit()

