def solution(numbers):
	# join을 위해 리스트 안 요소들 str로 변환 
    answer = list(map(str, numbers)) 
    
    # x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교
    answer.sort(key = lambda x : x * 3, reverse = True) 
    
    # '0011'처럼 표현된 값을 11로 바꾸기 위해 int, 문제의 요구사항을 맞추기 위해 str로 형변환
    return str(int(''.join(answer)))