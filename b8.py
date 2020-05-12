class Bank:
    Account_type = "savings"
    location = "Guntur"
    def __init__(self, name, Account_number,balance):
        self.name = name
        self.Account_number + Account_Number
        self.balance=balance
        self.Account_type=Bank.Account_type
        self.location=Bank.location
    def _repr__(self):
        print ("wwelcome to  the SBI ATM Machine")
        print("-----------------------------------------------")
        account_pin = int (input("Please enter your pin Number"))
        if(account_pin==123):
            Account(self)
        else:
            print("pin incorrect. please try again")
            error(self)
            return ' ',join([self.name,self.Account_Number])
    def Error(self):
        account_pin = int(input("please enter your pin number")
        if(account_pin==123) 
            Acccount(self)
        else:
            print("pin Incorrect. please try again")
            Error(self)
    def Account(self):
            print("Your card number is:XXXX XXXX XXXX 1337")
            print("Would you like to deposit/withdraw/check balance")
            print("""
    1) Balance
    2) Withdraw
    3) Reposit
    4) Quit
    """)
            option=int (input("please enter your choice"))
            if(option==1):
                balance(self)
            elif(option==2):
                Withdraw(self)
            elif(option==3):
                deposut(self)
            elif(option==4):
                exit()
        def Balance(self):
            print("Balance:",self.balance)
            Account(self)
        def Withdraw(self):
            w=int(input("please enter desired amount: "))
            if(self.balance>0 and self .balance>=w):
                self.balance=self.balance=w
                print("your transaction is successfull")
                print("Amount is not sufficient in your account")
            Account(self)
        def Deposit(self):
            d=int(input("pleasr enter desired amount:"))
            self.balance=self.balance+d
            print("Your transaction is successfull")
            print("Balance:",self.balance)
            Account(self)
        def Exit():
            print ("Exit")
        t1 = bank('mahesh', 1453210145,5000)
        print (t1)
                
            
        
        
