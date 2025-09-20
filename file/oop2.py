#delete 
#second part of loop
'''class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("karan")
print(s1.name)
del s1.name
print(s1.name)  # This will raise AttributeError

 
#private attribute
class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #private attribute

def reset_pass(self):
    print(self.__acc_pass)

acc1 = Account("12345","abcd")
print(acc1.acc_no)
print(acc1.__acc_pass)  # this will raise attribute error


class Person:
    __name = "anonymous"

    def __hello():
        print("hello person")

        def welcome(self):
           self. __hello()

    p1 = Person()

    print(p1.__welcome())  # this will raise attribute error

#inheritance
#multilevel inheritance
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand

        class Fortunere(ToyotaCar):
            def __init__(self,type):
             self.type = type

             car1 = Fortunere("disel")
             car1.start()

 #multiple inheritance
class A:
    varA = "welcome to class A"

class B:
  varB = "welcome to class B"

class C(A,B):
   varC = "welcome to class C "
   c1 = c()

   print(c1.varC)
   print(c1.varA)
   print(c1.varB)

#super method
class Car:
  def __init__(self,type):
       self.type = type
    

@staticmethod
def start():
        print("car started")

@staticmethod
def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name,type):
       
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius","electrical")
print(car1.type)


#class method

class Person:
    name = "anonymous"

    #def changeName(self,name):
       # Person.name = name

    @classmethod
    def changeName(cls,name):
        cls.name = name

        p1 = Person()
        p1.changeName("nabin damase")
        print(p1.name)
        print(Person.name)

      #property
       
       
class Student:

       def __init_(self,phy,chem,math):
              self.phy = phy
              self.chem = chem
              self.math = math
              self.percentage = str(self.phy+self.chem+self.math)/3 +"%"

              
@property
def percentage(self):
              return str(self.phy+self.chem+self.math)/3 +"%"

              stu1 = Student(98,96,99)
              print(stu1.percentage)

              stu1.phy=86
              
              print(stu1.percentage)'''









