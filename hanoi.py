def towerOfHanoi(n,source,spare,target):
    '''
    objective: To Solve the problem of tower of hanoi.
    input parameters:
        n: Number of Disk
        source: The source of the disk
        spare: A spare to move the disk
        target: The Target to move the disk
    return value: none
    approach: If n is 1 Move disk from source to target
              Else subtract 1 from n and move disk from source to spare
    '''
    if n == 1:
        print('Move disk from ',source,'to',target)

    else:
        towerOfHanoi(n-1,source,target,spare)
        print('Move disk from ',source,'to',target)
        towerOfHanoi(n-1,spare,source,target)

def main():
    '''
    objective: To Solve the problem of tower of hanoi.
    input parameters:
        n: Number of Disk
        source: The source of the disk
        spare: A spare to move the disk
        target: The Target to move the disk
    return value: none
    approach: Use the hanoi Function
    '''
    n = int(input('Enter the number of disk: '))
    towerOfHanoi(n,source=1,spare=2,target=3)
    

if __name__=='__main__':
    main()
