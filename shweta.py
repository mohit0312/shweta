def insert_fun(num,list1):
    ''' Objective: to insert a no. in a sorted list
        input parameter: a no. to be inserted
        output: a list after adding the desired no. given
    '''
    #approach: using recursion
    
    length = len(list1)
    print(length)
    if length == 0:
        list1.append(num)
        return list1
    else:
        for i in range (0,length-1) :
            if(list1[i] < num) :
                i+=1
        i=i+1    
        ele = list1[i]
        list1[i]=num
        num=ele
        insert_fun(num,list1[1:])
            

    return list1

listp = [1,2,3,5,6]
value = 4

insert_fun(value, listp)

