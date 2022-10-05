def arithmetic_arranger(lst):
    t1,t2,t3,maxxterm,calc=[],[],[],[],[]
    arranged_problems=""
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
        if t1[i].isdigit() == False or t3[i].isdigit() == False:
            raise TypeError("Error: Numbers must only contain digits.")
        elif t2[i] not in ['+','-']:
            raise TypeError("Error: Operator must be '+' or '-'.")
        elif len(t1[i])>4 or len(t1[i])>4:
            raise TypeError("Error: Numbers cannot be more than four digits.")
    for i in range(length):
        arranged_problems+="  "+t1[i].rjust(maxxterm[i])+"    "
    arranged_problems+="\n"
    for i in range(length):
        arranged_problems+=t2[i]+" "+t3[i].rjust(maxxterm[i])+"    "
    arranged_problems+="\n"
    for i in range(length):
        arranged_problems+='-'*(maxxterm[i]+2)+"    "
    for i in range(length):
        if t2[i]=='+':
            calc.append(int(t1[i])+int(t3[i]))
        elif t2[i]=='-':
            calc.append(int(t1[i])-int(t3[i]))
    arranged_problems+="\n"
    for i in range(length):
        arranged_problems+=str(calc[i]).rjust(maxxterm[i]+2)+"    "
    return arranged_problems