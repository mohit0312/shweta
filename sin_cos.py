epsilon = 0.0001
def cos(x):
    '''
       objective: to find the value of cos(x)
       input parameters : x is given by user
       return value: value of cos(x)
    '''
    term=1
    total=1
    multiplyby= -x**2
    nextterm=1
    while abs(term)>epsilon:
        divide=(nextterm)*(nextterm+1)
        term=(term*multiply)/divide
        total+=term
        nextterm+=2
    return total
def sin(x):
    '''
       objective: to find the value of sin(x)
       input parameters : x is given by user
       return value: value of sin(x)
    '''
    term=x
    total=x
    multiplyby= -x**2
    nextterm=1
    while abs(term)>epsilon:
        divide=(nextterm)*(nextterm+1)
        term=(term*multiplyby)/divide
        total+=term
        nextterm+=2
    return total
def main():
    '''
       objective: to find the value of cos(x) and sin(x)
       input parameters : x is given by user
       return value: none
    '''
    angle = float(input('enter the angle'))
    a=(angle*3.1415926535823846)/180
    print('enter yr choice')
    print('1-sin(x)')
    print('2-cos(x)')
    c=int(input("enter ur choice"))
    if c==1:
        print("value of sin(x)",sin(a))
    elif c==2:
        print("value of cos(x)",cos(a))
        
if __name__=='__main__':
    main()
print("end of program")    
