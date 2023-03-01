num=int(input("enter the number"))
sum=0
temp=num
while(temp>0):
    digit= temp%10
    sum=sum+digit*digit*digit
    temp=temp//10
if (sum==num):
    print("it is arm strong number")
else:
    print("it is not a arm stong")