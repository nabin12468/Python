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


  
def calc_sum(num,price,tax):
    price_n = num*tax
    final_tax = price_n-num

    print("total", final_tax)

calc_sum(10,20,30)

'''