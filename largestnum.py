#Finding the largest value in a list.
largest=0
for thing in [25,78,38,92,75]:
    if thing>largest:
        largest=thing
    print(largest,thing)
print("The largest number is:",largest)
