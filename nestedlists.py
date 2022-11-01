lst=[]
scr=[]
nam=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scr.append(score)
        lst.append([name,score])
    scr.sort()
    mini=min(scr)
    for i in range(0,len(scr)):
            if scr[i] != mini:
                k=scr[i]
                break
    for i in lst:
        if i[1] == k:
            nam.append(i[0])
    nam.sort()
    for i in nam:
        print(i)
