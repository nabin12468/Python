#functin

'''def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(5,6)
calc_sum(10,20)

#def calc_sum(a,b):
    return a+b

sum=calc_sum(178,20)
print(sum)

#average
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg
avg=calc_avg(10,20,30)
print(avg)


#print("my name is ghansham ghana"),end=""
print("i am from nepal")'''





#default parameters

'''def cal_prod(a,b=2):
    print(a*b)
    return a*b
cal_prod(10)
cal_prod(10,5)


#practice

cities=["kathmandu","pokhara","butwal","biratnagar"]
heroes=["batman","superman","ironman","spiderman"]

print(heroes[0],end="")
print(cities[2], end="")

def print_len(list):
    print (len(list))

def print_list(list):
    for val in list:
        print(val,end=" ")

        print_list(heroes)
        print()



#waf to find factorial of n.(n is the parameter)

n=5
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
result=factorial(6) 

#waf to convert usd to npr.
def converter(usd_val):
    
    npr_val=usd_val*130
    print(npr_val,"USD=",npr_val,"NPR")

    converter(133)'''





#Recursion

'''def show(n):
    if(n==0):  #base case
     return
    print(n)
    show(n-1)
    print("END")

show(5)

#new one
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
    print(fact(5))

#write a recursive function to calculate the sum of first n natural numbers.
def sum (n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
print(sum(5))
#write a recursive function to print all elememnts in a list.






