# 중요도는 높을수록 중요
# a b c d  2
# 1 2 3 4

# 1 1 9 1 1 1 
# a b c d e f
# 9 1 1 1 1 1
# c d e f a b

n = int(input())

# target이 언제 나가느냐.. -> target 위치가 -1이 될때 cnt값
for i in range(n):
    num, target = map(int, input().split())
    case = list(map(int, input().split()))
    cnt = 0

    while target != -1 :
        if (max(case) == case[0]):
            case.pop(0)
            cnt += 1
            target -= 1  # 앞으로 한 칸 땡겨짐
        else :
            case.append(case[0])
            case.pop(0)

            # target이 제일 앞에 있지만 max가 아니라면 target 맨뒤로 보냄
            if target == 0 and (max(case) != target) :
                target = len(case) - 1
            elif target == 0 and (max(case) == target):
                cnt += 1
                break
            else :
                target -= 1

    print(cnt)
        