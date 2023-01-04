# 부등호

n = int(input())
sign = list(input().split())
# 방문 표시
visited = [False] * 10
# 최댓값, 최솟값
max_ans, min_ans = "", ""

# 연산자 계산
def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j

# 최댓값과 최솟값 구하기
def solve(cnt, s):
    global max_ans, min_ans
    # 부등호의 개수 + 1만큼 문자열이 구성되었다면
    if cnt == n + 1:
    	# 최솟값이 존재하지 않다면
        if not len(min_ans):
        	# 최솟값으로 추가
            min_ans = s
        # 그 외에는 최댓값
        else:
            max_ans = s
        return
    # 숫자를 0부터 9까지 1개씩 입력받아
    for i in range(10):
    	# 특정 숫자를 아직 방문하지 않았다면
        if not visited[i]:
        	# 문자열이 아직 존재하지 않거나, 계산이 가능한 경우
            if cnt == 0 or possible(s[-1], str(i), sign[cnt - 1]):
            	# 방문 표시
                visited[i] = True
                # 문자열 개수 1개 추가
                solve(cnt+1, s + str(i))
                # 방문 표시 제거
                visited[i] = False
# 함수 실행
solve(0, "")
# 최댓값 출력
print(max_ans)
# 최솟값 출력
print(min_ans)


## 두번째 풀이
# from itertools import permutations

# k = int(input())
# signs = input().split()

# result = []
# for per in permutations([0,1,2,3,4,5,6,7,8,9],k+1) :
#   flag = True
#   for i in range(len(signs)) :
#     if signs[i] == '<' :
#       if per[i] < per[i+1] : continue
#       else : 
#         flag = False
#         break
#     else :
#       if per[i] > per[i+1] : continue
#       else : 
#         flag = False
#         break
#   if flag :
#     result.append(per)

# print(''.join(map(str,list(max(result)))))
# print(''.join(map(str,list(min(result)))))