class User:

    bankname = "Mi bankito"
    allUsersaccounts = []

    def __init__(self, accountNum, owner):
        self.accountNum = accountNum
        self.owner = owner
        self.balance = 0.0
        User.allUsersaccounts.append( self )

    def withdraw_acc( self, amount ):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "You have not enought funds to proceed with the transaction." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )


    def printUsersinfo( self ):
        print (f"User: {self.owner}, Balance: ${self.balance}")

    def deposit_acc( self, amount ):
        self.balance += amount


