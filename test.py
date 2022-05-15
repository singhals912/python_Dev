class Employee:

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@email.com"

        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(int(self.pay)*self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
         super().__init__(first, last, pay)
         if employees is None:
             self.employees=[]
         else:
            self.employees = employees
        

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)  

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)  

    def print_employees(self):
        for emp in self.employees:
            print('-->',emp.fullname())



dev_1 = Developer('sachin', 'singhal', 5000, "Python")
dev_2 = Employee('astha', 'goyal', 10000)

mgr_1 = Manager('Sue','Smith',8000,[dev_1])
print(mgr_1.email)
mgr_1.add_employee(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_employees()
# print(dev_1.first)
# print(dev_1.prog_lang)


# print(dev_1.pay)
# Employee.apply_raise(dev_1)
# print(dev_1.pay)

# print(Employee.no_of_emps)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_string_1 = 'hey-bro-6000'
# new_emp_1=Employee.from_string(emp_string_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)
# Employee.apply_raise(new_emp_1)
# print(new_emp_1.pay)

# import datetime
# my_date = datetime.date(2016,8,28)

# print(Employee.is_workday(my_date))
