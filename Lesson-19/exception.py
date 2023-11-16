
class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("This just in't cool,main.")
    # print(x/1)
    # raise Exception("I'm customer exception")
    # if not type(x) is str:
    # raise TypeError("Only string allowed")
except NameError:
    print('NameError mean something is probably in not undefined')
except ZeroDivisionError:
    print('Please do not divide by zero')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error")

# Exception in w3 school
