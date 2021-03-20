def x(a):
    global s
    def s(a):
        c=a*a
        return c
a=int(input("enter the number: "))
x(a)
print(s(a))


#without global
def x(a):
    def s(a):
        c=a*a
        return c
    print(s(a))
a=int(input("enter the number: "))
x(a)
