import prob3

end = 20

rst=[]
stk=[]
result=1


for i in range(2,end+1):

    factors = prob3.get_factor(i)
    for f in factors:
        if f not in rst:
            rst.append(f)
            result *= f
        else:
            rst.remove(f)
            stk.append(f)
    while len(stk) != 0:
        rst.append(stk.pop())
    while len(factors) !=0:
        factors.pop()


print result
    # nextprime()
    # if prime[-1]
    # print i