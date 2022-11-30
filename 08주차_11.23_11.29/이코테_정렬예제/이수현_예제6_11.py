# 6-11 : 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 점수만 정수형으로 변환
    array.append((input_data[0], int(input_data[1])))

# 키를 이용하여 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])