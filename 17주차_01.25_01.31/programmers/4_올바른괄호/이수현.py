# 올바른 괄호
# https://velog.io/@ssongplay/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%AC%EB%B0%94%EB%A5%B8-%EA%B4%84%ED%98%B8-Python

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            # 괄호 짝이 ')'로 시작하면 False
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []