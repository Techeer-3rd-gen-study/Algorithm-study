# 공유기 설치
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split()) # 집의 개수, 공유기 개수
home_list = sorted([int(input().rstrip()) for _ in range(N)])

start = 1 # 공유기 사이 거리 최소값
end = home_list[-1] - home_list[0] # 공유기 사이 거리 최대값
ans = 0

while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    router = home_list[0] # 공유기 초기 설치 위치
    router_num = 1 # 공유기 개수

    for i in range(1, N):
        if home_list[i] >= router + mid:
            router = home_list[i] # 공유기 위치 변경
            router_num += 1
    
    if router_num >= C: # c개 이상의 공유기를 설치할 수 있는 경우, 공유기 사이 거리 증가
        start = mid + 1
        ans = mid
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(ans)
