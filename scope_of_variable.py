#Scope of variable in nested function
def f1(): 
    s = 'I love Navgurukul Family'
      
    def f2(): 
        print(s) 
          
    f2() 
f1() 

#with return

def x():
    a="I love my family"

    def y():
        return a
    b=y()
    print(b)
x()
