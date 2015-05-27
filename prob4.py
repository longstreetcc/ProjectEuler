

for i in range(999,99,-1):
    flag = False
    a=i/100
    b=i%100/10
    c=i%10
    pal = c * 100 + b * 10 + a  + i*1000

    for j in range(999,99,-1):

        yu = pal % j
        ch = pal /j
        if yu == 0 and ch > 99 and ch <1000:
            print pal ," = ", i ,"*", j
            flag = True
            break
    if flag == True:
        break