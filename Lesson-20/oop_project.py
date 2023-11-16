from Bank_Account import *

Dave = BankAccount(1000, "D4ve")
Sara = BankAccount(4000, "Sara")

Dave.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(100)


Dave.transfer(10000, Sara)
Dave.transfer(10, Sara)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Balze = SavingsAcct(1000, "Blaze")

Balze.getBalance()
Balze.deposit(100)
Balze.transfer(1000, Sara)
