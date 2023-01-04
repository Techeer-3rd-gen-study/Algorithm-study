# 2529 : 부등호
# https://data-flower.tistory.com/76

n = int(input())
sign = list(input().split())
# 방문 표시할 리스트
visited = [False] * 10
# 최댓값, 최솟값
ans_max, ans_min = "", ""

# 연산자 계산
def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j
    return True

# 최댓값과 최솟값 구하기
def solve(cnt, s):
    global ans_max, ans_min
    # 부등호 개수 + 1만큼 문자열이 구성되었다면
    if cnt == n + 1:
        # 최솟값이 존재하지 않다면
        if not len(ans_min):
            ans_min = s
        # 그 외에는 최댓값
        else:
            ans_max = s
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
                solve(cnt + 1, s + str(i))
                # 방문 표시 제거
                visited[i] = False

# 함수 설정
solve(0, "")
# 최대, 최솟값 출력
print(ans_max)
print(ans_min)