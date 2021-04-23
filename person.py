class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)

    def __str__(self):
        return self.name + ' is ' + str(self.age)


class Employee(Person):
    def __init__(self, name, age, e_id):
        # this super init refers to the parent class
        super().__init__(name, age)
        self.e_id = e_id

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay

    def __str__(self):
        # by calling super here we eliminate duplicated code
        return super().__str__() + ' - id ' + str(self.e_id) + ')'


class SalesPerson(Employee):
    def __init__(self, name, age, e_id, region, sales):
        super().__init__(name, age, e_id)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.5


if __name__ == "__main__":
    print('Person')
    p = Person('John', 54)
    print(p)
    print('-' * 25)
    print('Employee')
    e = Employee('Denise', 51, 7468)
    e.birthday()
    print(e)
    print('e.calculate_pay(40):', e.calculate_pay(40))
    print('-' * 25)
    print('SalesPerson')
    s = SalesPerson('Phoebe', 21, 4712, 'UK', 30000.0)
    s.birthday()
    print('s.calculate_pay(40):', s.calculate_pay(40))
    print('s.bonus():', s.bonus())
