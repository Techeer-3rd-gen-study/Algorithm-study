# 6-12 : 두 배열의 원소 교체

n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()                   # 오름차순 정렬
b_list.sort(reverse = True)     # 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a_list[i] < b_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
    else:
        break

print(sum(a_list))