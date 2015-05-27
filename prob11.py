f = open('/Users/Cai/Desktop/test.txt','r')

num=[]
adjacent = 4
temp=[]
digit = ' '
while digit != '':
    digit = f.read(2)

    temp.append(digit)

    digit = f.read(1)
    if digit == '\n':
        num.append(temp)
        temp=[]
num.append(temp)

print num

print len(num),len(num[0])

print num[-1]


maxmul = 1


for i in range(0,len(num)):
    for j in range(0,len(num[0])):

        if i + adjacent <= len(num):
            multi = 1
            for k in range(0,adjacent):
                multi *= int(num[i+k][j])
            if multi > maxmul:
                maxmul = multi

        if j + adjacent <= len(num[0]):
            multi = 1
            for k in range(0,adjacent):
                multi *= int(num[i][j+k])

            if multi > maxmul:
                maxmul = multi

        if (i + adjacent <= len(num)) and (j + adjacent <= len(num[0])):
            multi = 1
            for k in range(0,adjacent):
                multi *= int(num[i+k][j+k])

            if multi > maxmul:
                maxmul = multi

        if (i + adjacent <= len(num)) and (j - adjacent >= 0):
            multi = 1
            for k in range(0,adjacent):
                multi *= int(num[i+k][j-k])

            if multi > maxmul:
                maxmul = multi

print maxmul



