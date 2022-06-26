score=input("Enter the sore: ")
score=float(score)
try:
        if score<=1.0:
                if score>=0.9:
                    print("The grade obtained is:","A")
                elif score>=0.8:
                    print("The grade obtained is:","B")
                elif score>=0.7:
                    print("The grade obtained is:","C")
                elif score>=0.6:
                    print("The grade obtained is:","D")
                elif score<0.6:
                    print("Failed")
        else:
            print("Score entered has exceeded the expected range.")
except:
        print("The score entered is lower than the excepted range. Please try again.")
