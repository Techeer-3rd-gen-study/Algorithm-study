# 카펫

def solution(brown, yellow):
    total = brown + yellow                  # a * b = total
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            
            a = total / b                   # total / b = a
            if a >= b:                      # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a,b]