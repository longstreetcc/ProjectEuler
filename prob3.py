
# num = 600851475143



rst=[]
# i=2
# for j in range(i,num):
#     if num % j == 0:
#         rst.push(j)
#         num=num / j
#         break

prime = [2]

def nextprime():
    i = prime[-1]+1
    while True:
        flag = True
        for p in prime:
            if i % p == 0:
                flag=False
                break
        if flag == False:
            i+=1
        else:
            prime.append(i)
            break



def get_factor(num):
    while True:
        f=True
        for i in prime:
            if num % i ==0:
                rst.append(i)
                num = num / i
                f=False
        if f==True:
            nextprime()
        if num in prime or num ==1:
            rst.append(num)
            break
    while rst.count(1) != 0:
        rst.remove(1)
    return rst


if __name__ == '__main__':
    num=5
    print get_factor(num)










#   test next prime
# for i in range(0,5):
#     nextprime()
# print prime