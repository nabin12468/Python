
#__init__ function
'''class Student:
    name = "nabin"

    #default constructor
    #def __init__(self):
        #print("hello")

    #parameterized constructor

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print(self)
        print("hello")

S1 = Student("karan")
print(S1.name)

s2 = Student("rohan")
print(s2.name,s2.marks)

# S2 = Student()
# print(S2.name)'''


#class & Instance Attributes

'''class Student:
        
        college_name = "ABC college"  #class attribute
        name="anonymous"   #instance attribute
def __init__(self, name,marks):
        self.name = name
        self.marks = marks
       
        print("hello my name is nabin damase")

S1 = Student("karan",90)
print(S1.name)

#methods in class
class Student:
        
        college_name = "ABC college"  #class attribute
        name="anonymous"   #instance attribute
def __init__(self, name,marks):
        self.name = name
        self.marks = marks
       
        print("hello my name is nabin damase")




#static method & class method

#@staticmethod
#def info():
    #print("this is student class")

#abstraction in python
        class car:
        def__init__(self):
        self.name = False
        self.brk = False
        self.clutch = False

def start(self):
    self.name = True
    self.acc=True
    print("car started")

 car1 = car()
 car1.start()'''

# practice

class Account:
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
        print("hello",self.name)

    def deposit(self, amt):
        self.balance+=amt
        print("deposited",amt)

    def withdraw(self, amt):
        if self.balance>=amt:
            self.balance-=amt
            print("withdrawn",amt)
        else:
            print("insufficient balance")

    def check_balance(self):
        return self.balance