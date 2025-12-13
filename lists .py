#lists


''''marks =[99,94,91,93,97]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])'''

'''students = ["nabin",98,99.99,"kathmandu"]
print(students[0])
students[0]="ram"
print(students)
'''
#list slicing
'''marks =[99,94,91,93,97]
print(marks[1:4])
print(marks[0:])
print(marks[:3])'''

#list methods

'''list =[1,2,3,]
list.append(4)
print(list)'''

#sorting method

'''marks=[8,3,5,6,7]
#print(marks.sort())     #ascending order
#print(marks.sort(reverse=True))  #decending order
#marks.reverse()   #reverse the list
#marks.insert(9,1)
marks.pop(2)

print(marks)'''


#Tuples



#practice
#wap to ask the userto enter names of their 3 favorite movies & store them in a list

'''movies = []
mov1=input("enter your 1st favorite movies: ")
mov2=input("enter your 2nd favorite movies: ")
mov3=input("enter your 3rd favorite movies: ")

movies.append(mov1)
movies.append(mov2) 
movies.append(mov3)
print(movies)'''









#wap to check if a list contains a palindrome of elements.

list=[1,2,1]

list2=[1,2,3]
copy_list=list.copy()
copy_list.reverse()
if(list==copy_list):
    print("palindrome")
else:
    print("not a palindrome")

