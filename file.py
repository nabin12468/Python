#file handling

'''

f=open("file.txt","a")

f.write("Hello World")

f.close()


with open("file.txt","r") as f:
    data=f.read()
    print(data)

    with open("file.txt","w") as f:
        f.write("Hello World")

        #delete file

import os
os.remove("file.txt")'''

#practice

#check the word in the file or not


def  check_for_word():
 word ="learning"
with open("file.txt","r") as f:
    data=f.read()
    
    if(data.find(word) !=-1):
        print("word found")
    else:
        print("word not found")

        def check_for_line():
            word ="learning"
            data=True
            line_no=1
            with open("file.txt","r") as f:
                while data:
                    data=f.readline()
                
                if(word in data):
                    print(f"word found in line {line_no}")
                    line_no+=1

                    return -1
               print(check_for_line())













