n = int(input())
if n <= 0:
    exit()

up_card_list = [0] * 263 
down_card_list = [0] * 263 

for _ in range(n):
    a = int(input())
    if a >= 0:
        up_card_list[a] += 1
    elif a < 0:
        down_card_list[-1 * a] += 1


max_up = max(up_card_list)
max_down = max(down_card_list)
max_down_result = -1

[i for i,v in enumerate(down_card_list) if v == max_down]
for i, v in enumerate(down_card_list):
    if v != 0 and max_down_result < i :
        max_down_result = i

if max_up == max_down :

    print(-1 * max_down_result)
elif max_up > max_down :
    print(up_card_list.index(max_up))
elif max_up < max_down :
    print(-1 * max_down_result)


