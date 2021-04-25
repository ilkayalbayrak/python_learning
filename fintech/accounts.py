from abc import ABC

import fintech.errorHandling as err
import abc


class Account(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'account_number') and
                callable(subclass.account_number) and
                hasattr(subclass, 'account_holder') and
                callable(subclass.account_holder) or
                hasattr(subclass, 'balance') and
                callable(subclass.balance) or
                hasattr(subclass, 'deposit') and
                callable(subclass.deposit) or
                hasattr(subclass, 'withdraw') and
                callable(subclass.withdraw) or
                NotImplemented)

    # instance_count = 0
    #
    # @classmethod
    # @abc.abstractmethod
    # def increase_instance_count(cls):
    #     cls.instance_count += 1
    #
    # @classmethod
    # @abc.abstractmethod
    # def print_instance_count(cls):
    #     print("Current instance count: {}".format(cls.instance_count))

    # def __init__(self, account_number, account_holder, balance):
    #     # self.increase_instance_count()
    #     # self.print_instance_count()
    #     self._account_number = account_number
    #     self._account_holder = account_holder
    #     self._balance = balance
    #     self._acc_type = self.__class__.__name__

    @property
    @abc.abstractmethod
    def account_number(self):
        raise NotImplementedError

    @account_number.setter
    @abc.abstractmethod
    def account_number(self, value):
        raise NotImplementedError

    @account_number.deleter
    @abc.abstractmethod
    def account_number(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def account_holder(self):
        raise NotImplementedError

    @account_holder.setter
    @abc.abstractmethod
    def account_holder(self, value):
        raise NotImplementedError

    @account_holder.deleter
    @abc.abstractmethod
    def account_holder(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def balance(self):
        raise NotImplementedError

    @balance.setter
    @abc.abstractmethod
    def balance(self, value):
        raise NotImplementedError

    @balance.deleter
    @abc.abstractmethod
    def balance(self):
        raise NotImplementedError

    @abc.abstractmethod
    def deposit(self, amount):
        raise NotImplementedError
        # else:
        #     raise Exception(" Deposit amount should be a float > 0")
        # # return self.balance

    @abc.abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError
        # return self.balance


class DepositAccount(Account):

    def __init__(self, account_number, account_holder, balance, interest_rate):
        self._balance = balance
        self._account_holder = account_holder
        self._account_number = account_number
        self._interest_rate = interest_rate
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

    def withdraw(self, amount):
        if isinstance(amount, float) and amount > 0:
            self._balance -= amount
        else:
            raise err.AmountError(amount)

    def __str__(self):
        return "Acc_Type: " + str(self._acc_type) + " - Acc_Number: " + str(
            self._account_number) + " - Acc_holder: " + self._account_holder + " - Balance: " + str(
            self._balance) + " - Interest_rate: " + str(self._interest_rate)


class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        self._account_holder = account_holder
        self._account_number = account_number
        self._balance = balance
        self._overdraft_limit = overdraft_limit
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
        return "Acc_Type: " + str(self._acc_type) + " - Acc_Number: " + str(
            self._account_number) + " - Acc_holder: " + self._account_holder + " - Balance: " + str(
            self._balance) + "- Overdraft_limit: " + str(self._overdraft_limit * -1)


class InvestmentAccount(Account):

    def __init__(self, account_number, account_holder, balance, investment_type):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        self._investment_type = investment_type
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

    def withdraw(self, amount):
        if isinstance(amount, float) and amount > 0:
            self._balance -= amount
        else:
            raise err.AmountError(amount)
        # return self.balance

    @property
    def investment_type(self):
        return self._investment_type

    @investment_type.setter
    def investment_type(self, inv_type):
        if isinstance(inv_type, str):
            self._investment_type = inv_type
        else:
            raise TypeError("Investment type should be str")

    @investment_type.deleter
    def investment_type(self):
        del self._investment_type

    def __str__(self):
        return "Acc_Type: " + str(self._acc_type) + " - Acc_Number: " + str(
            self._account_number) + " - Acc_holder: " + self._account_holder + " - Balance: " + str(
            self._balance) + "- Investment-type: " + self._investment_type
