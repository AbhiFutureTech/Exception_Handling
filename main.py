# Exceptions are errors detected at the time of program execution
# In exception code we expect the as zero

# x is string and y is integer
x = input("Enter number1: ")
y = input("Enter number2: ")
try:
    z = x/int(y)
except Exception as e:
    print('exception occured : ',e)
    z = None
except TypeError as e:
    print('type error exception')
    z = None
print("Division: ",z)
