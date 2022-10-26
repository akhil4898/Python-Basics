# import os

# # import something...


# print("Hello World...")
# a = 50
# b = a
# print(a)
# print(b)


# print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.''')




# for playing sound...

# from playsound import playsound
# playsound('/home/akhil/Documents/Python/maa.mp3')




# import os
# print(os.listdir())   #It will show the list of items in dir...




# Variable...

# b = '''Akhil'''
# c = None
# d = True
# e = 45.24
# f = 234



# printing variables...

# print(b) 
# print(c) 
# print(d) 
# print(e) 
# print(f)



# Printing the data type of variables...

# print(type(b))
# print(type(c)) 
# print(type(d)) 
# print(type(e)) 
# print(type(f))



# Operators..

# a = 23
# b = 7
# print("Value of a+b is: ", a+b)

# a -= 3  # a = a + 7
# print(a) 


# A = (14 != 3)   # It returns boolean value...
# print(A)

# bool1 = True
# bool2 = False
# print("The value of bool1 and bool2 is: ", (bool1 and bool2))
# print("The value of bool1 or bool2 is: ", (bool1 or bool2))
# print("The value of not bool2 is: ", (not bool2))





# Type casting and type()

# a = "23440"
# a = int(a) #String to int
# print(a + 5)
# b = 123
# b = str(b) #int to string
# print(b)
# c = 123
# c = float(c) #int to float
# print(c)
# d = 34.56
# d = int(d)
# print(d)





# Input function

# value = input("Enter your value: ")
# value = int(value)   #Convert a to integer
# print(type(value))
# print("The value is:", value)




# To print remainder... 

# a = 19
# b = 2
# c = a % b
# print("the remainder when a is divided by b is:", c)




# program to calculate square
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# print(type(a), " ", type(b))
# print("The Addition value is:", a + b)





# Strings

# name = "Akhil Upadhyay"
# surname = "Upadhyay"
# print(name + "", surname)
# print(name[0])
# print(len(name))     # To find length of variable...
# print(name[0:4])       # String Slicing 
# print(name[:4])
# print(name[1:])
# print(name[-4:-3])
# print(name[1:8:2])    #Here, 2 is skip value...






# String functions

# print(len(name))
# print(name)
# print(name.find("Upadhyay"))     # If not present (return -1)...
# print(name.endswith("Upadhyay"))
# print(name.count("h"))
# print(name.capitalize())
# print(name.replace("Upadhyay", "Nikhil"))






# name = input("Enter your name: ")
# print("Good Morning, " + name)




# To print date

# from datetime import date, datetime
# from datetime import datetime
# import datetime
# print(date.today())       #from datetime import date
# print(datetime.now())     #from datetime import datetime
# current_time = datetime.datetime.now()     #import datetime
# print(current_time.year)
# print(current_time.month)
# print(current_time.day)
# print(current_time)




# letter = '''Name: <|Name|>
# Greetings from Credgenics. I am happy to tell you about your selection.
# You are selected!

# Have a great day ahead!
# Date: <|Date|>
# '''

# name = input("Enter your name: ")
# d = input("Enter date: ")

# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", d)
# print("") 
# print(letter)






# name = "This is Akhil Upadhyay.  I am your friend..  "
# finds = name.find("  ")
# if(finds > 0):
#     print("True") 

# else:
#     print("False")

# # rep = name.replace("  ", " ")
# print(name.replace("  ", " "))



# letter = "Dear Akhil,\n \t This python course is nice. \nThanks!"
# print(letter)








# List..

# a = [1,"Akhil",3,4.23,True]
# print("List elemets are:", a)
# a[0] = 100
# print("List elemets are:", a)
# print(a[1])
# print(a[1:5])            #List Slicing 
# print(a[-4:])



# Methods of Lists


l1 = [1,5,3,7,7,9]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.reverse()
l1.append(30)
print(l1)
l1.insert(2,201)    # To insert element in list using index and value.
print(l1)
l1.pop(2)           #To remove element fom list using index value.
print(l1)
l1.remove(7)        #To remove element from list using element value.
print(l1)