# 입력값 3개 받아오기 A, B 는 아예 리스트로 처음부터 받아오기
n=int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0 

for _ in range(n): # n번 반복하면서 문제에 제시된 함수 s 구현 A[0]* B[0]
    sum += A.pop(A.index(min(A))) * B.pop(B.index(max(B))) 
    # 리스트의 최소값,최대값의 인덱스를 구해서 pop을 통해 없애가며 계속 구함

print(sum)