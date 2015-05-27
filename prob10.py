import prob3

end = 2000000
while prob3.prime[-1]<end:
    prob3.nextprime()
prob3.prime.pop()
sum=0
for i in prob3.prime:
    sum+=i

print sum