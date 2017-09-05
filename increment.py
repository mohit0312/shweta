def increment(n):
    '''
       objective: to increment a no.
       input parameters: a number
       output: incremented no.
    '''
    return(n+1)
def sum(num1,num2):
    '''
       objective : to obtain sum of two non negative no.s
       input parameters : first number
                          second number
       output : sum of numbers
    '''
    if(num1>0 and num2>0):
      if(num1>num2):
         if(num2!=0):
           increment(num1)
           num2=num2-1
         else:
           return(num1)
      elif(num2>num1):
         if(num1!=0):
           increment(num2)
           num1=num1-1
      else:
         if(num1!=0):
           increment(num2)
           num1=num1-1
