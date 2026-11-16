def main ():
    P = float (input("Enter the account's present value:"))
    while P <0:
        print("Present value cannot be negative.")
        P = float(input("Enter the account's present value"))

    i = float (input("Enter user monthly intrest rate"))
    while i <0:
        print("Monthly intrest rate cannot be negative.")
        i = float(input("Enter the monthly interest rate: "))
    
    
    t = int(input("Enter the number of months that the money will be left in the account: "))
    while t <=0:
        print("Number of months must be greater than zero.")
        t = int(input("Enter the number of months that the money will be left in the account:"))

    f = futureValue(P,i,t)

    print("The account's future value is: $" +format(f,".2f"))

def futureValue(P,i,t):
    f=P*(1+i)**t
    return f

main()