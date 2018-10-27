#reverse function

list2=[]
def rec(list1):
    length=len(list1)
    if list1==[]:
        return list2
    
    else:
        '''
        '''
        list2.append(list1[length-1])
        return rec(list1[0:length-1])
