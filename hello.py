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

# takeInput = input("Enter input: ")
# if takeInput == "maa":
#     playsound('/home/akhil/Documents/Python/maa.mp3')
# elif takeInput == "Ankh":
#     playsound('/home/akhil/Documents/Python/Ankh.mp3')
# else:
#     print("Sorry... This song is not available...")




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
# Creating List with []...

# a = [1,"Akhil",3,4.23,True]
# print("List elemets are:", a)
# a[0] = 100
# print("List elemets are:", a)
# print(a[1])
# print(a[1:5])            #List Slicing 
# print(a[-4:])



# Methods of Lists


# l1 = [1,5,3,7,7,9]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.reverse()
# l1.append(30)
# print(l1)
# l1.insert(2,201)    # To insert element in list using index and value.
# print(l1)
# l1.pop(2)           #To remove element fom list using index value.
# print(l1)
# l1.remove(7)        #To remove element from list using element value.
# print(l1)








# Tuple
# Creating tuple using ()


# a = (1, 7, 6, 4, 1, 1, 1)
# print(a)
# print(a[2])
# a[2] = 12      #'tuple' object does not support item assignment

# t1 = (1,)         # Tupl wwith one element...
# print(t1)
# t2 = ()             # Empty tuple
# print(t2)


# Methods of tuple..

# print(a.count(1))
# print(a.index(6))






# Programs..

# l1 = []
# print(l1)
# n = int(input("Enter number of fruits: "))
# for i in range(0, n):
#     fruits = input("Enter element: ")
#     l1.append(fruits)
# print(l1)


# l2 = []
# n = int(input("Enter number of Students: "))
# for i in range(0, n):
#     Marks = int(input("Enter Marks: "))
#     l2.append(Marks)
# l2.sort()
# print(l2)


# li = [2, 3, 4, 5]
# sum = 0
# for i in li:
#     sum = sum + i
# print(sum)


# a = (7,0,8,0,0,9,0)
# findZeros = a.count(0)
# print(findZeros)







# Dictionary....





# myDic = {
#     "Akhil": "Coder",
#     "Rahul": "Data Engineer",
#     "Mohan": "Engineer",
#     "Marks": [1,2,3,4],
#     "tup": (4, 5, 6),
#     "dic": {"Harish": "CEO"},
#     1: 2
# }
# print(myDic)
# print(myDic['Akhil'])
# print(myDic['dic']['Harish'])
# print(myDic['tup'])
# myDic["Marks"] = [23, 34, 45]
# print(myDic['Marks'])




# Methods of Dictionary
# print(type(myDic.keys()))       # print type of dictionary...
# print(list(myDic.keys()))       # print elements of dictionary in list form..
# print(myDic.keys())
# print(myDic.values())
# print(myDic.items())
# print(myDic)
# updateDic = {
#     "Raja": "Rani",
#     "Pen": "Paper"
# }
# myDic.update(updateDic)
# print(myDic)

# print(myDic.get("Raja"))










# Sets...

# a = {1,2,4,5,4,3}         # It cannot store duplicate values and give output in sorted order...
# print(a)
# print(type(a))

# b = {}                     # It creates the empty dictionary not empty set..
# print(type(b))


# c = set()                   # It creates the empty set..
# print(type(c))
# c.add(12)                   # we can add items here like this...
# c.add(11)
# c.add(3)
# c.add(78)
# # c.add([1,2,3])            #we cannot add list and dictionary to sets..beacause they are changeable or unhashable...
# # c.add({"Akhil": "Upadhyay"})
# c.add((1 ,2 ,3))
# print(c)
# print(len(c))
# c.pop()
# print(c)
# print(len(c))
 





# Programs...

# myDic = {
#     "pushtak": "Book",
#     "ghadi": "Watch",
#     "topi": "Cap" 
# }
# print("Options are: ", myDic.keys())
# a = input("Enter the hindi word: ")
# print("The meaning of hindi word is:", myDic.get(a))



# s1 = set()
# print(type(s1))
# n = int(input("Enter the size of set: "))
# for i in range(0, n):
#     takeInput = int(input("Enter number: "))
#     s1.add(takeInput)
# print(list(s1)) 


# s1 = {18, "18"}
# print(type(s1))
# print(len(s1))



# s = set()
# s.add(20)
# s.add("20")
# s.add(20.0)             # It takes 20.0 as 20...
# print(len(s))           # we are having 2 elements in set.. 


# s = {}                      # S is of dictionary type...
# print(type(s))  




# dic = {}
# n = int(input("Enter number of friends: "))
# for i in range(0, n):
#     takeName = input("Enter name: ")
#     takeColor = input("Enter color: ")
#     # dict = {takeName: takeColor}
#     # dic.update(dict)
#     dic[takeName] = takeColor   
# print(len(dic))
# print(dic)



# s = {10, 5, 2, (2,3,6), 4}          # we can only add tuples in sets..because tuples are immutable.
# print(len(s))
# print(s)    





# Conditional Expressions...

# age = int(input("Enter age: "))
# if(age >= 18):
#     print("Yes")
# else:
#     print("No")

# if(age is 18):          # Shows warning But will executed..
#     print("Yes")
# else:
#     print("No")

# s = [1, 2, 3]
# if 10 in s:
#     print("True")
# else:
#     print("False")




# Programs

# ls = []                                     #Create empty list...
# n = int(input("Enter size of numbers: "))
# for i in range(0, n):
#     element = int(input("Enter Number: "))
#     ls.append(element)                      #append elements in list....
# max = ls[0]
# for i in range(0, n):   
#     if (ls[i] > max):                       #find maximum element in list...
#         max = ls[i] 
# print("The Largest number is:", max) 



# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
# num3 = int(input("Enter number: "))
# num4 = int(input("Enter number: "))

# if num1 > num4:
#     f1 = num1
# else:
#     f1 = num4

# if num2 > num3:
#     f2 = num2
# else:
#     f2 = num3

# if f1 > f2:
#     print("The greatest number is:", f1)
# else:
#     print("The greatest number is:", f2)




# sub1 = int(input("Enter marks: "))
# sub2 = int(input("Enter marks: "))
# sub3 = int(input("Enter marks: "))
# sum = (sub1 + sub2 + sub3) / 3

# if (sub1 < 33 or sub2 < 33 or sub3 < 33):
#     print("You are fail")
# elif (sum < 40):
#     print("You are fail")
# else:
#     print("Congratulations! you passed the exam with", sum, "percentage...")
    



# text = input("Enter text: ")

# if ("make a lot of money" in text):
#     spam = True
# elif ("buy now" in text):
#     spam = True
# elif ("click this" in text):    
#     spam = True    
# elif ("subscribe this" in text):
#     spam = True
# else:
#     spam = False


# if (spam):
#     print("This is spam...")
# else:
#     print("This is not spam...")



# name = input("Enter name: ")
# length = len(name)
# if(length < 10):
#     print("Contain less than 10 characters in name...")
# else:
#     print("Contain more than 10 characters in name...")





# l1 = ["Akhil", "Mohan", "Sohan", "Ramu", "Shyam"]
# takeInput = input("Enter name to find in the list: ")
# if(takeInput in l1):
#     print("Element found...")
# else:
#     print("Element not found...")        





# myDic = {
#     "90 - 100": "Ex",
#     "80 - 90": "A",
#     "70 - 80": "B",
#     "60 - 70": "C",
#     "50 - 60": "D",
#     "40 - 50": "E",
#     "10 - 40": "Fail"
# }
# marks = (input("Enter marks: "))
# if(marks in  myDic):
#     print("Your grade is: ", myDic.get(marks))




# marks = int(input("Enter marks: "))
# if marks > 90:
#     grade = "Ex"
# elif marks > 80:
#     grade = "A"
# elif marks > 70:
#     grade = "B"
# elif marks > 60:
#     grade = "C"
# elif marks > 50:
#     grade = "D"
# else:
#     grade = "Fail"

# print("Your grade is: ", grade)









