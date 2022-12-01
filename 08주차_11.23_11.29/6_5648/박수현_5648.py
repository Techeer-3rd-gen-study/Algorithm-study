import sys

li = list()
cnt = 0
while 1:
    try:
        ins = input()
        if ins == -1:
            break
        else:
            i_sp = ins.split()
            for i in i_sp:
                if cnt != 0:
                    i = "".join(reversed(i)).lstrip("0")
                    li.append(int(i))
                cnt += 1
    except EOFError:
        break

res = sorted(li)
for i in res:
    print(i)