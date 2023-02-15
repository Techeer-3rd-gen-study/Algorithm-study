def solution(brown, yellow):
    answer = []
    
    s = brown + yellow # 전체 넓이
    # width * height  = brown + yellow
    
    width = s - 2 # 너비 초기값
    while True:
        if s % width == 0 :
            height = s // width
            if width <= 2 or height <=2:
                width -= 1
                continue
            y = (width - 2) * (height - 2)
            if brown == s - y:
                if height <= width :
                    answer= [width, height]
                    break
                else :
                    answer = [height, width]
                    break
            else:
                width -= 1
                pass
        else:
            width -= 1
            pass
    
    return answer