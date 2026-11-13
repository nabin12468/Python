'''def tool():
      print("This is a tool function.")
   
      tool()
 
    
    

def check_price():
         price=90
         if price > 70:
                 print("okay")

         else:
          print("not okay")
          


check_price()




#parameters

def check_price(price):
    if price > 70:
        print("okay")
    else:
        print("not okay")

check_price(90)




def print_name(name, age):
    print("my name is",name,age)

print_name("Alice",30)





def number(num):

    print("the number is",num)

    number([1,2,3,4,])


def calc_sum(B=12,A="19"):

    print(A+B)

    calc_sum(B="10")


amount = 100 #global variable
  
def calc_sum(num,price,tax):
    amount = 100  #local variable
    price_n = num*amount
    final_tax = price_n-num

    print("total", final_tax)

calc_sum(10,20,30)


amount




def hey(a, b):

    print(a+b)

    hey(5, 10)

    def hey_return(a, b):
        return a + b

    result = hey_return(5, 10)
    print(result)
    print(result)
'''

def double(num):
    return num * 2

result = double(5)


total = double(10) + double(20)

print("Total:", total, "Result:", result) ''''''