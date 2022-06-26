#Program to prompt the user for hours and pay per hours to compute gross pay.
hrs=input("Enter the number of hours:")
hrs=float(hrs)
pay=input("Enter the rate per hour:")
pay=float(pay)
if hrs<=40:
        grosspay=hrs*pay
elif hrs>40:
        grosspay=(40*pay)+(1.5*pay*(hrs-40))
print("The gross pay is:",grosspay)
