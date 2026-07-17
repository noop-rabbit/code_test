class BankAccount:
  def __init__(self, balance: float):
    self._balance = balance


  @property
  def balance(self):
    return self._balance

  def deposit(self, amount):

    if amount <= 0:
      raise ValueError("Amount must be greater than 0")
    else:
      self._balance += amount


  def withdraw(self, amount):

    if amount <= 0:
      raise ValueError("Amount must be greater than 0")
    elif self._balance >= amount:
      self._balance -= amount

    else:
      raise ValueError("Insufficient balance")

account = BankAccount(1000)
print(account.balance)
#account.balance = 500    --> Not possible to set externally like this

account.deposit(100)
print(account.balance)
account.withdraw(300)
print(account.balance)
#account.withdraw(-20)
#print(account.balance)
#Learnings
# property makes balance readable like an attribute (account.balance, no parentheses)
# but since there's no matching @balance.setter, it's not writable from outside. That's the mechanism, not just the intent.
# if only the current method needs it temporarily, keep it local; if another method or
# the object's identity needs to persist/reference it later, promote it to self.X.