# 올바른괄호

def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True