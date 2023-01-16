# 파일 정리

import sys
input = sys.stdin.readline

N = int(input().rstrip())
file = {} # 딕셔너리 생성

for _ in range(N):
    filename = input().rstrip().split('.') # filename[0] = 파일명, filename[1] = 확장자
    
    if filename[1] in file: # 확장자가 file에 있는 경우
        file[filename[1]] += 1 # +1
    else: # 확장자가 file에 없는 경우
        file[filename[1]] = 1 # 확장자 추가 & 1로 설정

file = sorted(file.items(), key = lambda x:x[0], reverse=False) # 확장자 사전순 출력

for i in file:
    print(i[0], i[1]) # 파일명, 개수 출력