class AmountError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "AmountError(Cannot deposit negative amounts: " + str(self.amount) + ")"


class BalanceError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "BalanceError(Cannot exceed the overdraft limit while withdrawal: " + str(self.amount) + ")"
