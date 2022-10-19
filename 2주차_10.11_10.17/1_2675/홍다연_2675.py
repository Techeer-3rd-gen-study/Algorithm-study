# 2675 문자열 반복 

T = int(input())   # 테스트 케이스 개수 

for i in range (T) :
    R,S = input().split()  # R:반복 횟수 / S:문자열 
    for letter in S :
        # split은 문자열의 형식으로 두 변수 저장해주기 때문에, int로 R을 바꿔줘야 함 , split에 map으로 int 설정시 둘다 되므로 에러
        print(letter*int(R),end="") 
    print()

