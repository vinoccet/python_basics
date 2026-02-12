print("divide by zero")
try:
    file=open("error.txt","r")
    ...
    number=int(input("Enter the number: "))
    value=10/0
    print(value)
except  ZeroDivisionError as error:
    print("actual error ")       
except ValueError as error:
    print("except input as a valid number")   
except FileNotFoundError as f_error :
    
    print("file not found") 
# finally:
#     file.close()    

class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age<0:
        raise InvalidAgeError("Provide a positve number for age")
    print(age)

try:
    set_age(-1)
except  InvalidAgeError as error:
    print(error)       