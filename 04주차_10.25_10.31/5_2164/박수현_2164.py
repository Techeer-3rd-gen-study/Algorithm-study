##### 시간초과된 방법 #####

# import sys

# input = sys.stdin.readline

# num = int(input())

# num_list = list(range(1, num+1))

# while len(num_list)!=1:
#     num_list.pop(0)
#     temp = num_list[0]
#     num_list.pop(0)
#     num_list.append(temp)

# print(num_list[0])


##### 큐를 이용하여 성공한 방법 #####

import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
num_queue = deque()

for i in range(num):
    num_queue.append(i + 1)

while len(num_queue) > 1:
    num_queue.popleft()
    num_queue.append(num_queue.popleft())

print(num_queue.pop())
