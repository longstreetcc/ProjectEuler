

for a in range(1,1000):
    asqr = a*a
    for b in range(a,1000):
        c=1000-a-b
        if c <= a or c <= b:
            continue
        if c*c == asqr + b*b:
            print a*b*c