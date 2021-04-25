from abc import ABC

import fintech.accounts as accounts
# import fintech.errorHandling as error

import abc

from abc import ABC





if __name__ == "__main__":
    acc1 = accounts.CurrentAccount(74, "ilkay", 800, 500)
    acc2 = accounts.DepositAccount(74, "ilkay", 800, 1.6)
    acc3 = accounts.InvestmentAccount(74, "ilkay", 800, "high risk")
    print(acc1.__str__())
    print(acc2.__str__())
    print(acc3.__str__())
    print(issubclass(accounts.CurrentAccount, accounts.Account))
    print(isinstance(acc1, accounts.Account))

    with accounts.CurrentAccount('891', 'Adam', 5.0, 50.0) as acc:
        acc.deposit(23.0)
        acc.withdraw(12.33)
        print(acc.balance)


    # class MyABC(ABC):
    #     pass
    #
    #
    # MyABC.register(tuple)
    #
    # assert issubclass(tuple, MyABC)
    # print(issubclass(tuple, MyABC))
    # assert isinstance((), MyABC)
    # print(isinstance((), MyABC))

# class Account(metaclass=abc.ABCMeta):
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
#
# def __init__(self, account_number, account_holder, balance):
#     self.increase_instance_count()
#     self.print_instance_count()
#     self._account_number = account_number
#     self._account_holder = account_holder
#     self._balance = balance
#     self._acc_type = self.__class__.__name__
#
# @property
# @abc.abstractmethod
# def account_number(self):
#     return self._account_number
#
# @account_number.setter
# @abc.abstractmethod
# def account_number(self, value):
#     if isinstance(value, int) and value >= 0:
#         self._account_number = value
#     else:
#         raise Exception("account_number should be an integer value >= 0")
#
# @account_number.deleter
# @abc.abstractmethod
# def account_number(self):
#     del self._account_number
#
# @property
# @abc.abstractmethod
# def account_holder(self):
#     return self._account_holder
#
# @account_holder.setter
# @abc.abstractmethod
# def account_holder(self, value):
#     if isinstance(value, str):
#         self._account_holder = value
#     else:
#         raise Exception("account_holder value has to be a string")
#
# @account_holder.deleter
# @abc.abstractmethod
# def account_holder(self):
#     del self._account_holder
#
# @property
# @abc.abstractmethod
# def balance(self):
#     return self._balance
#
# @balance.setter
# @abc.abstractmethod
# def balance(self, value):
#     if isinstance(value, float) and value > 0:
#         self._balance = value
#
# @balance.deleter
# @abc.abstractmethod
# def balance(self):
#     del self._balance
#
# @abc.abstractmethod
# def deposit(self, amount):
#     if isinstance(amount, float) and amount > 0:
#         self._balance += amount
#     else:
#         raise err.AmountError(amount)
#     # else:
#     #     raise Exception(" Deposit amount should be a float > 0")
#     # # return self.balance
#
# @abc.abstractmethod
# def withdraw(self, amount):
#     if isinstance(amount, float) and amount > 0:
#         self._balance -= amount
#     else:
#         raise err.AmountError(amount)
#     # return self.balance
#
# def __str__(self):
#     return "Acc_Type: " + str(self._acc_type) + " - Acc_Number: " + str(
#         self._account_number) + " - Acc_holder: " + self._account_holder + " - Balance: " + str(self._balance)
