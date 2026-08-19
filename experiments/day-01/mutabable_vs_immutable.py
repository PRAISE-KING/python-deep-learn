# mutability answers the question if the object can be updated or not/ can python create a new object or keep using the existing one incase od a change of value

# <--- IMMUTABLE --->
# are those that cannot be updated after they are created instead python creates a new object incase of an update or change
# they include :
# str
# int
# float
# tuple
# bool

# example
x = 38
# here x ---> integer object ---->value(38)
x = 41
# python will create another object integer x --> integer object --> value(41)

# these rules apply to all other immutble types


# <--- MUTABLE --->
# they can be changed or updated
# python will always update them rather than creating a new object
# they include:
# list
# dictionary
# set

# example using lists
numbers = [1,2,3]
print(numbers)

numbers.append(4)
print(numbers)
# python does not creat the new list object but instead update the existing one 
# this applies to all mutable objects in python


# >>>>>>>>>>>>>>>>>> EXERCISE <<<<<<<<<<<<<<<<<<<<<<
name = 'Billionaire Praiseking'
print(id(name))

name += ' Ochieng'
print(name)
print(id(name))
# here since string is immutable the name will add to the new name and form one name then python creates a new string object and rebinds name to the new list object


a = [1, 2]
b = a

b = [10, 20]

print(a)
print(b)

print(id(a))
print(id(b))
# here a and b share the same list object at first
# = sign is always an assignment sign and so
# even though lists are mutable in this case its not about changing or updating or mutating but assignment and so
#  b rebinds to a new list object so python creates a new list object for b 
# in the end a and b will refer to different list objects and have different id and values 

