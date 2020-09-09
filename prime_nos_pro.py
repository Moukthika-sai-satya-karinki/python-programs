#prime numbers up to a specified limit
start=int(input('enter the starting value from which prime nos have to be printed'))
last=int(input('enter the end limit'))

for i in range(start,last):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)    