
end = 100

squaresum=0
sum=0

for i in range(1,end+1):
    squaresum += i*i
    sum+=i

sumsquare=sum*sum

diff = sumsquare - squaresum

print diff
