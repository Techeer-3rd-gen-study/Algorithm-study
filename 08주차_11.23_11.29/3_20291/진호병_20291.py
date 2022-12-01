N = int(input())

file_list = {}

for _ in range(N):
    filename, extension = input().split(".")
    if extension in file_list:  
        file_list[extension] += 1
    else :
        file_list[extension] = 1

result = sorted(file_list.items(), key=lambda x : x[0])


for x in result:
    print(x[0],x[1])