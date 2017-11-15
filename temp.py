z=int(input("Enter the no. of elements:"))
p=n=0
for i in range(1,z+1):
    x=int(input("Enter the number:"))
    if(x==-1):
        break;
    elif(x<0):
        n=n+1;
    elif(x>0):
        p=p+1;
print("The frequency of negative numbers is",n)
print("The frequency of positive numbers is",p)