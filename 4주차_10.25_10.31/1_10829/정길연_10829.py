# 23 / 2  1
# 11 / 2  1
# 5  / 2  1
# 2  / 2  0
# 1
# 10111 
# 16 4 2 1

target = int(input())
binary_num_li = list()

# (+) format()사용 -> 'b' : binary
# binaryNum = format(target, 'b')
# print(binaryNum)

while (target > 1) :
    binary_num_li.append(target%2)
    target //= 2

binary_num_li.append(1)
binary_num_li.reverse()


# for i in binary_num_li:
#     print(i, end="")
print("".join(str(e) for e in binary_num_li))

# (x) print("".join(binary_num_li))
# 이거는 모~든 요소가 string일때만 유효
