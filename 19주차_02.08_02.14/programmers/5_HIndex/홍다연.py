# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747#

def solution(studys):
    studys.sort(reverse=True)
    for idx , study in enumerate(studys):
        if idx >= study:
            return idx
    return len(studys)