class Account():
	
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self,amount):
		self.balance = self.balance + amount
		print(f"New balance is ${str(self.balance)}")

	def withdrawl(self,amount):
		if self.balance >= amount:
			self.balance = self.balance - amount
			print(f"New balance is ${str(self.balance)}")
		else:
			print("Sorry Insuficient funds")

	def __str__(self):
		return f'Account owner: {self.owner}\nAccount balance: ${str(self.balance)}.'


acct = Account('Robert',200)

# print(acct)
# print(acct.owner)
# print(acct.balance)


acct.withdrawl(350)
acct.deposit(100)
acct.withdrawl(300)

print(acct)