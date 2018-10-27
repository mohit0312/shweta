import sys
sys.path.append('/home/administrator/Desktop/mca_101/shweta_mca101')
import rect_sq_tri    
def main():
    '''
       objective : to find the area of rectangle,square and triangle
       input parameters :
                    length:length of rectangle
                    breadth: breadth of rectangle
                    side of square
                    base of triangle
                    height of triangle
       return value: no return value
    '''
    print("enter yr choice")
    print("1 - area of rectangle")
    print("2 - area of square")
    print("3 - area of triangle")
    c=int(input("enter choice"))
    if c==1:
        a= int(input("enter length of rectangle"))
        b= int(input("enter breadth of rectangle"))
        print("area of rectangle is ", rect_sq_tri.arearectangle(a,b))
    elif c==2:
        a=int(input("enter side of square"))
        print("area of square is",rect_sq_tri.areasquare(a))
    elif c==3:
        a= int(input("enter base of triangle"))
        b= int(input("enter height of triangle"))
        print("area of triangle is ", rect_sq_tri.areatriangle(a,b))
if __name__=='__main__':
    main()
print("end of program")    
