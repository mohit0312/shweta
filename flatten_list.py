i=0
def sort_fun(list1):
    '''
       Objective :to sort the list
       input parameters : list
       output : sorted list
    '''
    min=list1[i]
    for i in range(len(list1)) :
         if (min>list1[i+1]) :
             temp= min
             min=list1[i+1]
             list1[i+1]=temp
         i=i+1
    
    
    
         
