total = int(input())

count = 0

for _ in range(total) : 
    arr = []
    word = list(input())
    result = "true"

    for j in range(len(word)) : 
        if word[j] not in arr:
            arr.append(word[j])
        else :
            if word[j-1] != word[j]:
                result = "false"
            else :
                arr.append(word[j])
                
    if result == "true" : 
        count += 1


                 
print(count)

