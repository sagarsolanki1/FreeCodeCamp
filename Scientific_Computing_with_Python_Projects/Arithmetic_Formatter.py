def arithmetic_arranger(lst):
    lnklst=[]
    t1=[]
    t2=[]
    t3=[]
    for i in range(0,len(lst)):
        lnklst.append(lst[i].split())
    for i in range(len(lnklst)):
        for j in range(3):
            if j==0:
                t1.append(lnklst[i][j])
            elif j==1:
                t2.append(lnklst[i][j])
            else:
                t3.append(lnklst[i][j])
    for i in range(len(t1)):
        if len(t1[i])>len(t3[i]):
            maxx=len(t1[i])
        else:
            maxx=len(t3[i])
        if i==0:
            print(" ",t1[i].rjust(maxx),"      ",end="")
            continue
        print(t1[i].rjust(maxx),"      ",end="")
    print("\n")
    for i in range(len(t1)):
        if len(t1[i])>len(t3[i]):
            maxx=len(t1[i])
        else:
            maxx=len(t3[i])
        print(t2[i],t3[i].rjust(maxx),"    ",end="")
    print("\n")
    for i in range(len(t1)):
        if len(t1[i])>len(t3[i]):
            maxx=len(t1[i])
        else:
            maxx=len(t3[i])
        print('-'*(maxx+2),"    ",end="")
    print("\n")
    for i in range(len(t1)):
        if len(t1[i])>len(t3[i]):
            maxx=len(t1[i])
        else:
            maxx=len(t3[i])
        if i==0:
            if t2[i]=='+':
                print(" ",(int(t1[i])+int(t3[i])),"      ",end="")
            elif t2[i]=='-':
                print(" ",(int(t1[i])-int(t3[i])),"      ",end="")
            continue
        if t2[i]=='+':
            print((int(t1[i])+int(t3[i])),"      ",end="")
        elif t2[i]=='-':
            print((int(t1[i])-int(t3[i])),"      ",end="")
