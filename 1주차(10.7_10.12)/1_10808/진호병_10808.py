alphabet = [0] * 26
n = input()

for i in n :
    alphabet[ord(i)-97] += 1

for j in range(len(alphabet)):
    print(alphabet[j], end=" ")