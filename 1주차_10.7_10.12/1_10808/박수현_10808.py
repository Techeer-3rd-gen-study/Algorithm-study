def strCount(str, char):
    return str.count(char)

def fromAToZ(str):
    countList = []
    for i in range(97, 123):
        countList.append(strCount(str, chr(i)))
    return countList

def countPrint(countList):
    for i in countList:
        print(i, end=' ')

if __name__ == "__main__":
    str = input()
    countPrint(fromAToZ(str))
