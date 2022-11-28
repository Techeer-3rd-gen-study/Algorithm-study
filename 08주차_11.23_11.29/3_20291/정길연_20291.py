n = int(input())
extension = {}

for i in range(n):
    file = input().split('.')[1]
    if file not in extension:
        extension[file] = 1
    else:
        extension[file] += 1

result = list(extension.keys())
result.sort()

for i in result:
    print(i, extension[i])
