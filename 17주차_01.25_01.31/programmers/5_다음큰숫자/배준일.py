def solution(n):
    binaryNum = bin(n)
    binaryNum = binaryNum[2:]
    
    while True:
        n += 1
        next_num = bin(n)[2:]
        
        if str(binaryNum).count('1') == str(next_num).count('1'):
            break
    
    return int(next_num, 2)
