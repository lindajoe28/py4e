#Computation of pay in a function that is defined and using this function to do the computation.
def computepay(hrs,pay):
        hrs=float(hrs)
        pay=float(pay)
        if hrs<=40:
                grosspay=hrs*pay
        elif hrs>40:
                grosspay=(40*pay)+(1.5*pay*(hrs-40))
        print("The gross pay is:",grosspay)
computepay(45,10.5)
