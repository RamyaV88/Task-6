# Problem 1 - Bank Account

class BankAccount: # Created a base class BankAccount with few attributes
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount): # Created a method deposit within the base class
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount): # Created a method withdraw within the base class
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self): # Created a method get balance within the base class to retuen the balance amount
        return self.balance

    def get_account_info(self): # Created a method get account info within the base class to retuen the account information
      return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}"

account1 = BankAccount("5455126458", "Mr. Alex Jane", 50000)
print(account1.get_account_info())

account1.deposit(1000) # Passing value to the method deposit
account1.withdraw(500) # Passing value to the method withdraw
print(account1.get_account_info()) # Printing the account details with the balance amount
print()

# Problem 2: Employee Management

class department: # Created a class department with few attributes
    def __init__(self, dept_ID, dept_name, location):
        self.dept_ID = dept_ID
        self.dept_name = dept_name
        self.location = location

    def print_department(self): # Printing the department details
        print("Department details:", self.dept_ID, self.dept_name, self.location)

ITdepartment = department(1, "IT", "Main building")
Findepartment = department(2, "Finance", "Main building")
Mardepartment = department(3, "Marketing", "Main building")

# Mardepartment.print_department()

class employee: # Created a class employee with few attributes
    def __init__(self, employee_ID, employee_name, dob, salary, title, dept_ID):
        self.employee_ID = employee_ID
        self.employee_name = employee_name
        self.dob = dob
        self.salary = salary
        self.title = title
        self.dept_ID = dept_ID

    def print_employee(self):  # Printing the employee details
        print("Employee Details:", self.employee_ID, self.employee_name,self.title)
        self.dept_ID.print_department()

emp1 = employee(101, "Anas", "31/01/1988",40000, "Marketing Manager", Mardepartment)
emp1.print_employee()
print()
emp2 = employee(102, "Benny", "05/04/1982", 50000, "IT Manager", ITdepartment)
emp2.print_employee()