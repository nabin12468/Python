#loop
'''print("hello world")
for i in range(1,11):
    print(i)

count=1
while count<=5:
    print("hello world")
    count+=1


#print number from 1 to 10

i=100
while i>=1:
    print(i)
    i-=1'''

#practice
'''nums=[1,2,3,4,5,6,7,8,9,10]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1


nums=[1,2,3,4,5,6,7,8,9,10]
x=5
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found")
        break
    else:
        print("not found")
    i+=1'''

#continue statement

'''i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
# for loop
name=["nabin","sabin","parbin","rabin"]
for val in name:
    print(val)


#practice
nums=[1,2,3,4,5,6,7,8]

idx=0


for el in nums:
    print(el)
    if el==5:
        print("number found at idx",idx)
        break
        idx+=1 

#range

#for i in range(1,11):
    #print(i)
#for i in range(1,11,2):
   # print(i)

for i in range(100,0,-1):
    #print(i)

#pass statement
for i in range(5):
    pass
print("hello world")'''





#practice
#wap to find the sum of first n natural numbers.(using while)

n=5
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
    
print("total sum =",sum)

#wap to find the factorial of a number (using for loop)

n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial =",fact)










    
    

