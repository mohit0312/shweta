def sum1(list):
    '''
       objective: to find the sum of elements of the list
       input parameters: list of elements
       output: sum of the elements
    '''
    #approach: using recursion
    sum=0
    if(list[0:]==[]):
        return sum
    else:
        sum=sum+list[0]+sum1(list[1:])
        return sum
