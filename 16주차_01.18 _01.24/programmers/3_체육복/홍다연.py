# 체육복

def solution(n, lost, reserve):
    
    reverseLost = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)
    
    for i in reverseLost :
        if i-1 in lost_del:
            lost_del.remove(i-1)
            
        elif i+1 in lost_del :
            lost_del.remove(i+1)
            
    answer = n - len(lost_del)
    
    return (answer)
