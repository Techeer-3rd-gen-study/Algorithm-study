# 20291 : 파일 정리

n = int(input())

file_dic = {}
file = [input().split('.')[1] for _ in range(n)]

# 확장자(키)가 파일 딕셔너리에 존재하면 
for i in file:
    if i in file_dic:
        file_dic[i] += 1
    # 존재하지 않으면 딕셔너리에 추가해주기
    else:
        file_dic[i] = 1
    
# 확장자와 파일 개수 둘 다 오름차순 정렬
# (첫 번째 요소, 두 번째 요소), 첫 번째 요소가 우선순위
result = dict(sorted(file_dic.items(), key = lambda x : (x[0], x[1])))

for k, v in result.items():
    print("{} {}".format(k, v))
