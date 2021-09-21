from User import User

pedroAccount = User( 12345, "Pedro Sanchez" )
julianAccount = User( 22222, "Julian Alvarez" )
amandaAccount = User( 54321, "Amanda Thriller" )

# print (User.allUsersaccounts)

julianAccount.deposit_acc(50000)
julianAccount.printUsersinfo()

amandaAccount.deposit_acc(1500)
amandaAccount.withdraw_acc(500)
amandaAccount.printUsersinfo()

pedroAccount.deposit_acc(5000)
pedroAccount.withdraw_acc(1000)
pedroAccount.printUsersinfo()


