f = open('/Users/Cai/Desktop/test.txt','r')

num=[]
adjacent = 13

digit = f.read(1)
while digit != '':
    if digit == '\n':
        digit = f.read(1)
        continue
    num.append(digit)
    digit = f.read(1)





maxmul = 1



for i in range(0,len(num)-adjacent):
    multi = 1
    for j in range(i,i+adjacent):
        multi *= int(num[j])
    if maxmul < multi:
        maxmul = multi
        for j in range(i,i+adjacent):
            print num[j],
        print '\n'







# multi = 1
# for j in range(0,adjacent):
#     multi *= int(num[j])
#
# maxmul = multi
#
# for i in range(adjacent,1000):
#     if num[i] == '0':
#
#     if int(num[i-adjacent]) != 0:
#         multi = multi / int(num[i-adjacent]) * int(num[i])
#     else:
#         multi = 1
#         for j in range(i-adjacent+1,i):
#             multi *= int(num[j])
#     print multi,maxmul
#     if multi > maxmul :
#         maxmul = multi

print maxmul