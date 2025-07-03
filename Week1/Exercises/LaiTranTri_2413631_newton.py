def find_squared_root (a):
    """ Find the squared root of number a """
    EPSILON = 0.001
    # TODO : Your code here
    xn=a
    xn1 = xn - (xn*xn-a)/(2*xn)
    while abs(xn1-xn)>=EPSILON:
        xn=xn1
        xn1=xn - (xn*xn-a)/(2*xn)
    return xn1

# TESTCASE
print("Test case 1: find_squared_root(2) → ",find_squared_root(2))
print("Test case 2: find_squared_root(3) → ",find_squared_root(3))