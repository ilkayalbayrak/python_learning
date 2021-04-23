import fintech.errorHandling as err


class Account:
    instance_count = 0

    @classmethod
    def increase_instance_count(cls):
        cls.instance_count += 1

    @classmethod
    def print_instance_count(cls):
        print("Current instance count: {}".format(cls.instance_count))

    def __init__(self, account_number, account_holder, balance):
        self.increase_instance_count()
        self.print_instance_count()
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        self._acc_type = self.__class__.__name__

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, int) and value >= 0:
            self._account_number = value
        else:
            raise Exception("account_number should be an integer value >= 0")

    @account_number.deleter
    def account_number(self):
        del self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, value):
        if isinstance(value, str):
            self._account_holder = value
        else:
            raise Exception("account_holder value has to be a string")

    @account_holder.deleter
    def account_holder(self):
        del self._account_holder

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, float) and value > 0:
            self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

    def deposit(self, amount):
        if isinstance(amount, float) and amount > 0:
            self._balance += amount
        else:
            raise err.AmountError(amount)
        # else:
        #     raise Exception(" Deposit amount should be a float > 0")
        # # return self.balance

    def withdraw(self, amount):
        if isinstance(amount, float) and amount > 0:
            self._balance -= amount
        else:
            raise err.AmountError(amount)
        # return self.balance

    def __str__(self):
        return "Acc_Type: " + str(self._acc_type) + " - Acc_Number: " + str(
            self._account_number) + " - Acc_holder: " + self._account_holder + " - Balance: " + str(self._balance)


class DepositAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        # self.increase_instance_count()
        Account.increase_instance_count()
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + " - Interest_rate: " + str(self.interest_rate)


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        # self.increase_instance_count()
        Account.increase_instance_count()
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, amount):
        if isinstance(amount, float) and amount >= 0:
            self._overdraft_limit = amount * -1

    @overdraft_limit.deleter
    def overdraft_limit(self):
        del self._overdraft_limit

    def withdraw(self, amount):
        if isinstance(amount, float) and (self.balance - amount) > self._overdraft_limit * -1:
            self.balance = self.balance - amount
        else:
            raise err.BalanceError(amount)

    def __str__(self):
        return super().__str__() + " - Overdraft_limit: " + str(self._overdraft_limit * -1)


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, balance, investment_type):
        super().__init__(account_number, account_holder, balance)
        Account.increase_instance_count()
        # self.increase_instance_count()
        self._investment_type = investment_type

    @property
    def investment_type(self):
        return self._investment_type

    @investment_type.setter
    def investment_type(self, inv_type):
        if isinstance(inv_type, str):
            self._investment_type = inv_type

    @investment_type.deleter
    def investment_type(self):
        del self._investment_type

    def __str__(self):
        return super().__str__() + " - " + self._investment_type
