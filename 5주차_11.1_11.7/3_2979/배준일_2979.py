# 트럭 주차

A, B, C = map(int, input().split())

A_time, B_time, C_time = list(map(int, input().split())), list(map(int, input().split())),list(map(int, input().split()))

start_times = [A_time[0], B_time[0], C_time[0]]
end_times = [A_time[1], B_time[1], C_time[1]]

now_time = min(start_times)

money = 0

for _ in range(max(end_times) - min(start_times) + 1):
    truck = 0

    for j in range(3): # 현재 시간에 있는 트럭 수 체크
        if start_times[j] <= now_time and end_times[j] > now_time:
            truck += 1
    
    if truck == 1:
        money += A * truck
    elif truck == 2:
        money += B * truck
    elif truck == 3:
        money += C * truck

    now_time += 1

print(money)

