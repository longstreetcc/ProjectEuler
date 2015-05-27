
sum=0

end = 4000000
i = 1
j = 2

while i < end and j < end:
    if i % 2 == 0:
        sum += i
    if j % 2 == 0:
        sum += j

    i = i + j
    j = i + j


if i < end and i % 2 == 0:
    sum += i


print sum

