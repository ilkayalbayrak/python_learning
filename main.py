import fintech.accounts as accounts
# import fintech.errorHandling as error

if __name__ == "__main__":
    acc1 = accounts.CurrentAccount(74, "ilkay", 800, 500)
    print(acc1.__str__())