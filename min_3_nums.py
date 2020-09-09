#python program for min of three numbers
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if(a<b and a<c):
    print(a,'a is smallest')
if(b<a and b<c):
    print(b,'b is smallest')
else:
    print(c,'c is smallest')        
