#Finding the average of numbers.
count=0
sum=0
for thing in [5,78,6,41,60,99]:
    count=count+1
    sum=sum+thing
    average=sum/count
    print(thing,average)
print("The final average is:",average)
