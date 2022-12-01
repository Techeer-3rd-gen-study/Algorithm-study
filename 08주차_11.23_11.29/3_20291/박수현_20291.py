num = int(input())

file_extention_dict = {}

for i in range(num) :
    file_extension = input().split(".")[1]
    if file_extension in file_extention_dict :
        file_extention_dict[file_extension] += 1
    else :
        file_extention_dict[file_extension] = 1

result = sorted(file_extention_dict.items())

for i in range(len(result)):
    print(result[i][0], result[i][1])