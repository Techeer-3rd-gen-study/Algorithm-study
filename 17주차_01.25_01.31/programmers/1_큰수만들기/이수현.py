# 큰 수 만들기
# https://hyunsix.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0%EC%88%98%EB%A7%8C%EB%93%A4%EA%B8%B0-python

def solution(number, k):
    answer = []
    for num in number:
        # 정답 리스트에 담긴 맨 뒷 숫자가 num 보다 작으면 제거        
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    # 슬라이싱
    return ''.join(answer[ : len(answer) - k])