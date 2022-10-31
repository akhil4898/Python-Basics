 # Multiline statement (\) denote that line should continue... 

# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))
# c = int(input("Enter num3: "))

# sum = a + \
#     b + \
#     c                                      

# print("the sum is:", sum)







# # Mutliple Assignment =>  allows you to assign single value to multiple variables...

# a = b = c = 1                                       # Assign one value to different variables...
# print(a, b, c)

# a, b, c = 1, 2.03, "Akhil"                          # Assign different values to different variables...
# print(a, b, c)







# # Mathematical Functions...

# import math

# x = 5
# print(abs(x))







# Random number function...

# import random

# seq = [1, 2, 5, 4, 3]
# print("Choices in numbers:", random.choice(seq))            # choice(seq) -> Gives random item from a list, tuple, or string...





# print(random.randrange(100, 1000, 3))                        # randrange(start, stop, step) -> selected element randomly form range... 






# print(random.random())                              # random() random value between (0<= r < 1)






# list = [20, 16, 10, 5]
# print("list: ", list)
# random.shuffle(list)                              # shuffle() -> randomizes the items of a list in place... 
# print("Reshuffled list: ", list)







# Strings => They are bunch of characters or set of characters...

# var1 = "Hello Akhil"
# var2 = "Python programming"
# print("var1: ", var1[0])
# print("var2: ", var2[1:])               
# print("var2: ", var2[:5])                           # Sliice Operator: [start : end]
# print("var is: ", var2[-4:])







# # Updating string....

# var1 = "Hello,World"
# print("Updated string: ", var1[:6] + "python")






# # String formatting Operator....

# name = "Akhil"
# w = 66.20
# age = 21
# print("My name is: %s and weight is: %d kg!" %(name,w))
# print("char is: %c and name is: %s and weight is: %d and age is: %d" %('A', name, w, age))








# Built-in String Methods...

# name = "akhil upadhyay"
# print(name.capitalize())                      # Capitalize() -> returns a copy of string with first character capitalized...







# Count() -> returns the number of occurance of substring sub in the range [start, end]

# sentence  = "This is Akhil Upadhyay, I a a programmer..."
# sub = "i"
# print(sentence.count(sub))
# sub = "This"
# print(sentence.count(sub))








# Decode() -> decode the string using the codec regisytered forencoding 

# name = "Akhil Upadhyay"
# name = name.encode('base64', 'strict')
# print("Encoded String: " + name)
# print("Decoding String: " + name.decode('base64', 'strict'))



































