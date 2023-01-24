# 가장 큰 수 

def solution(number):
    
    number = list(map(str, number))
    number.sort(key = lambda x : x*3, reverse = True)
    
    return str(int(''.join(number)))
