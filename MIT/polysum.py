import math

def polysum(n,s):
    perimeter = n*s
    area = (0.25*n*(s*s))/(math.tan(math.pi/n))
    #print perimeter
    sum = (area + (perimeter*perimeter))
    return round(sum,4)

print polysum(5,10)
