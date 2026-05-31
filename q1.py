#------Menu Driven Calculator----------#

def calculator():
    while True:
        print("\nWelcome to Calculator")
        print("Choices:")
        print("1. Addition , 2.Substraction, 3.Multiplication, 4.Division, 5.Exit")
        choice = input("select (1-5):")
        choices = ['1','2','3','4','5']



        if choice not in choices:
            print("Please Enter a Valid Operation (1-5):")
            choice = input("Enter:")
        if choice == '5':
            print("Exiting Calculator. GoodBye!!")
            break
        else:
            print(f"You selected option {choice}. Processing...")
            n1 = float(input("Num 1: ")); n2 = float(input("Num 2: "))

            if choice == '1': print("Result:", n1+n2)
            elif choice == '2': print("Result:", n1-n2)
            elif choice == '3': print("Result:", n1*n2)
            elif choice == '4': print("Result:", n1/n2 if n2 != 0 else "Error: Div by 0")
        

        

calculator()


