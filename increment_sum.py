def increment1(n):
    '''
       objective: to increment a no.
       input parameters: a number
       output: incremented no.
    '''
    n=n+1
    return n
def sum1(num1,num2):
    '''
       objective : to obtain sum of two non negative no.s
       input parameters : first number
                          second number
       output : sum of numbers
    '''
    if(num2!=0):
        num1=increment1(num1)
        return (sum1(num1,num2-1))
    else:
        return num1
   
