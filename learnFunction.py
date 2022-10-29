
# import string

# # def name(name: string, age: int = 23) -> string:                #Default argument...
# #     return "name is: " + name + " And age is: " + str(age)

# def name(name: string, age: int) -> string:
#     print(f"Name is: {name} and age is: {age}")

# # a = "Akhil"
# # b = 21
# # name(name = 'Akhil', age = 21)                                 # Keyword Arguments
# name(age = 23, name = "Nihkil")
# # print(myName)







#Variable-length arguments
#   1- *args (Non-Keyword Arguments)

#   2- **kwargs (Keyword Arguments) 





# def myFun(*argv):                                           # *args (Non-Keyword Arguments)
#     for arg in argv:
#         print(arg)

# myFun("Hello", "Akhil", "How", "Are you", "?")






# def myFun(**kwargv):                                           # **kwargs (Keyword Arguments) 
#     for key, value in kwargv.items():
#         print(f"{key} is {value}")

# myFun(name = "Akhil", surname = "Upadhyay", nickName = "lakhan")







# Docstring = The first string after the function is called the Document string
# Syntax: print(function_name.__doc__)


def toDescribe():
    '''This is the funtion to describe about the function...What it does...'''

print(toDescribe.__doc__)                                           # Docstring...
