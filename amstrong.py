num=int(input("Enter a number"))
sum=0
temp=num
while temp>0:
    res=temp %10
    sum += res *res*res
    temp = temp//10
if num == sum:
    print(num, "Amstrong number")
else:
    print(num, "not an amstrong number")

