#Finding the smallest number.
smallest=None
for value in [7,27,2,98,-7,98,33,-5,-12]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(value,smallest)
print("The smallest number is:",smallest)
