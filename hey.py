def outerFunction(text):    
    def innerFunction():  
        print(text)  
    
    innerFunction()  
text="Hey!"
outerFunction(text)