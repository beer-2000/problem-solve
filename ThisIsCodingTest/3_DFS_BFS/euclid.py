def gcdEuclid(a, b):
    if a % b == 0:
        return b
    else:
        return gcdEuclid(b, a % b)

print(gcdEuclid(192, 162))
