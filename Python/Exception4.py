##raise KeyboardInterrupt
##Traceback (most recent call last):
##
##KeyboardInterrupt
##
##raise MemoryError("This is an argument")
##Traceback (most recent call last):

##MemoryError:
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
