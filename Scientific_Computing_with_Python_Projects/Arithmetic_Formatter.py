def arithmetic_arranger(lst):
    t1,t2,t3,maxxterm,calc=[],[],[],[],[]
    if len(lst)>5:
        raise ValueError("Error: Too many problems.")
    else:
        for i in range(len(lst)):
            temp=lst[i].split()
            t1.append(temp[0])
            t2.append(temp[1])
            t3.append(temp[2])
    length=len(t1)
    for i in range(length):
        if len(t1[i])>len(t3[i]):
            maxxterm.append(len(t1[i]))
        else:
            maxxterm.append(len(t3[i]))
    for i in range(length):
        print("  "+t1[i].rjust(maxxterm[i]),end="    ")
    print("")
    for i in range(length):
        print(t2[i]+" "+t3[i].rjust(maxxterm[i]),end="    ")
    print("")
    for i in range(length):
        print('-'*(maxxterm[i]+2),end="    ")
    for i in range(length):
        if t2[i]=='+':
            calc.append(int(t1[i])+int(t3[i]))
        elif t2[i]=='-':
            calc.append(int(t1[i])-int(t3[i]))
    print("")
    for i in range(length):
        print(str(calc[i]).rjust(maxxterm[i]+2),end="    ")
