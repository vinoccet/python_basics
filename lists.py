names=["vinoth","ram","abdul"]
print(names[0].upper())

# changing values in list

#adding values to list
# insert()
# append()

# removing values 
# remove(value)
# .pop()
# del list[1]

# few other imp list methods
# len
# count
# index

phone_book=[{
    "name":"vinoth",
    "number":1234
},{
    "name":"ram",
    "number":2346
}]

phone_book[0].update({
    "name":"Alex",
    "number":1234
})

print(phone_book[0])