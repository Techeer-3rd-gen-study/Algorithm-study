total = int(input())

for _ in range(total):
    num , word = input().split()
    for i in range(len(word)): 
        for _ in range(int(num)):
            print(word[i], end="")
    print()