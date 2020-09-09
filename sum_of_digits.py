num=int(input('enter a number'))
total=0
while(n>0):
    digits=num%10
    total=total+digits
    num=num//10
print('the total number of digits',total)    


