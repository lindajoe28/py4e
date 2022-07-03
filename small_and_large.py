largest=None
smallest=None
#If we write while True the loop will run infinitely until there is a break statement.
while True:
    num=input("Enter a number: ")
    if num=="done":
        break
    try:
      num = int(num)
      if largest is None or largest < num:
          largest = num
      if smallest is None or smallest > num:
          smallest = num
    except:
      print('Invalid input')
      continue

print("Maximum is", largest)
print("Minimum is", smallest)
