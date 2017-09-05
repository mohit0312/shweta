def arearectangle(length,breadth):
   '''
   objective: to calculate the area of rectangle
   input:
         length and breadth of rectangle
   '''      
   # approach: multiply length and breadth
   
   area = length*breadth
   return area

def areasquare(side):
   '''
   objective: to calculate the area of square
   input:
         length of square
   approach: multiply side by itself
   '''
   return(arearectangle(side,side))
    
def main():
    '''
     objective: to calculate the area of square
     input: length of square
     approach: multiply side by side itself
    '''
    a = int(input("enter the length of a side"))
    print("area of square is",areasquare(a))
    print("end of output")

if __name__ == '__main__':
    main()
print("end of program")    
