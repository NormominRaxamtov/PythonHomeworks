# # name = input("What is your name?  ")
# # age = int(input("How old are you? "))

# # print(f"Your name is {name} and you are {age} years old")
# # print("Your name is " + name + " and you are " + str(age) + " years old") 
# # print("Your name is {a} and you are {b} years old".format(a=name, b=age))
# # print("Your name is {} and you are {} years old".format(age, name))

# # university = input("What university do you study? ")
# # year = input("what year are you in?  ")

# # print(f"You study at {university} and you are {year} year student") 
# # print("You study at {} and you are {} year student".format(university, year))
# # print("You study at " + university + " and you are " + str(year) + " year student")

# name = input("what is your name?  ")
# age = input("your age?   ")

# print(f"your name is {name} and you are {age}")
# print("your name is {} and you are {}".format(name, age))
# print("your name is " + name + " and you are " + str(age))
# print("")

# n = 45.345234097
# print (f"{n:.12f}")

# import random

# a =  int(input("Put any number: "))
# b =  int(input("put another number: "))
# print(f"Between {a} and {b} the random number is  ", end="") 
# print(random.randrange(a, b))

# n = 34.23456436
# print(f"{n:.6f}")


# name1 = "Kane"
# name2 = "Anderson"
# print(f"{name1:<14} - first name")
# print(f"{name2:<14} - second name")


# my_str = "Wassup Guys"
# print(len(my_str))
# print(my_str[:4] + my_str[7:])

# my_str = "I am just learning "
# print(my_str[::3])

# word = input("Word: ")

# last_word = word[-1]
# print(f"last word is : {last_word}", end="\n\n\n")
# print("last word is :", last_word, sep="  __  ")


fruit = "Apple banana"
print(fruit.lower())
print(fruit.upper())
print(fruit.capitalize())
print(fruit.title())

print(fruit.endswith('a'))
print(fruit.startswith('Ap'))


print('-'*50)
word = '      Heloooo MAAB      '
print(word)
print(word.strip())

print('--'*60)

fruits = "cherry apple banana"
print(fruits.split())