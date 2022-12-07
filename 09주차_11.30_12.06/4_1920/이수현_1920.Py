# 1920 : 수 찾기

n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    # 해당 수가 존재하는 지 확인
    if i in n_list:
        print(1)
    else:
        print(0)