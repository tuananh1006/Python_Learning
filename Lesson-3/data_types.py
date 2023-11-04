# String data type

# Linteral Assignment
import math
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# Press ctrl d to copy multi object
# pizza = str("Perreponi")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatentation
# last = 'Anh'
# first = 'Tuan'
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I like rock music from the ' + decade + "s."
print(statement)

# Multiple Lines
multipleline = '''
Hey, how are you?           

I was just checking in.                     
                            All good?
'''
print(multipleline)


# Escaping speacial characters
sentences = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentences)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multipleline.title())
print(multipleline.replace("good", "ok"))
print(multipleline)

print(len(multipleline))
multipleline += "                   "
multipleline = "                   "+multipleline
print(len(multipleline))

print(len(multipleline.strip()))
print(len(multipleline.lstrip()))
print(len(multipleline.rstrip()))

print(" ")
# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".")+"$1".rjust(4))
print("Muffin".ljust(16, ".")+"$2".rjust(4))
print("Chhesecake".ljust(16, ".")+"$4".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first)
print(first[1:-1])
print(first[1:])

# some methodes rutn boolean data
print(first.startswith("D"))
print(first.endswith("Z"))


# Boolean data type
myvalue = True
myvalue = False
x = bool(False)
print(type(x))
print(isinstance(x, bool))

# Numeric data types


# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in function for numbers

print(abs(-5))
print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to number
zipcde = '10001'
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemp to cast incorrect data
zipcode = 'hello'
