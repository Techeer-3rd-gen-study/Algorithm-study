def solution(number, k):
    stack = [] # 스택 만들기
    for n in number:
        while stack and stack[-1] < n and k > 0:
            # 스택이 비어있지 않고,
            # 스택의 제일 마지막 요소가 n보다 작고
            # k가 0보다 클 때 실행
            stack.pop() # 스택의 제일 마지막 요소 제거
            k -= 1 # k 제거
        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

solution("1231234", 3)