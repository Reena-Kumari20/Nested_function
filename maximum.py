#Write a Python function to find the Max of three numbers.
"""def max_of_three(a,b,c):
    if a>b and a>c:
        return(a," a is maximum")
    elif b>a and b>c:
        return(b,"b is maximum")
    elif c>a and c>b:
        return(c,"c is maximum")
    else:
        return("all equal")
a=int(input("num1: "))
b=int(input("num2: "))
c=int(input("num3: "))
x=max_of_three(a,b,c)
print(x)"""

#nested function

def max_two(a,b):
    if a>b:
        return a
    return b
def max_three(a,b,c):
    return max_two( a, max_two(b,c) )
print(max_three(3, 6, -5))


"""def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))"""
      
