'''
    objective: To flatten the list
    input parameters: the initial list to be flatten
                      the list in which the result to be stored
    result: the flattened list        
'''
def list_fun(list1,list2,i):
    if i==len(list1) :
        return list2
    elif type(list1[i])==list :
        list2.extend(list1[i])
        return list_fun(list1,list2,i+1)
    else:
        list2.append(list1[i])
        return list_fun(list1,list2,i+1)
    #i=i+1
    #return(list_fun(list1,list2,i))
    
l=[2,3,[8,4],7,[9,1]] 
m=[]
i=0
list_fun(l,m,i)   
