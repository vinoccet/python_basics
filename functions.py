
from functools import reduce
def greet_team(name):
    return f"Say hello to {name}"

message=greet_team("ram")    
print(message)

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

create_profile(21,"vinoth","cbe")    

def add(a):
    return a+10
# lambda arguments:body
add_by_10=lambda a:a+10
print(add_by_10(2))

numbers=[1,2,3,4,5]

#map,filter and reduce

squares=list(map(lambda x:x*2,numbers))
evens=list(filter(lambda x:x%2==0,numbers))

# acc=1 and x=2 => ist 1+2 =3
# acc=3 and x=3 => 2nd 3+3 = 6
# acc=6 and x=4 => 3rd 6+4 =10
# acc=10 and x=5 => 4th 10+5=15
sum=reduce(lambda acc,x:acc+x,numbers)
print(squares)
print(evens)
print(sum)


def combined_function(arg1, *args, **kwargs):
    print(f"Required argument: {arg1}")
    print(f"Positional arguments (tuple): {args}")
    print(f"Keyword arguments (dictionary): {kwargs}")
    for val in args:
        print(val)

combined_function("test",1,2,3,key1="value1", key2="value2")    