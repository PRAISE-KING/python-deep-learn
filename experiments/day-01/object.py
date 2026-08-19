# everything in python is an object
# everything including functions
# OBJECT ==> is a piece of memory in python that contains (type e.g int, value e.g 4, id(identity of the object))

# example
y = 22

print(type(y))
print(id(y)) 
print(y)  # value of integer object y



# 1.IDENTITY (id())
# answers the question Which exact object is this?
# Even if two objects have the same value, identity asks whether they're literally the same object.

# e.g in string 
v = 'Im a billionaire'
print(id(v))

# e.g in list
k = [56]
g = k

g.append(27) # i only updated g
print(k) # but k has the same update because i updated the same list object they share meaning they share an id
print(id(k))
print(id(g))


# 2.TYPE (type())
# this answers the question what exact type of an object is this?
# is it string or integer or bool or list etc

m = 'Im the richest billionaire'
t = 18.7
f = 13
u = [17]
l = True

print(type(m)) # str
print(type(t)) # float
print(type(f)) # int
print(type(u)) # list
print(type(l)) # bool



# 3.VALUE 
# is the actual content of the object
# eg
b = False
print(b)


# Exercise 
r = 10
print(id(r))

r = r+1
print (id(r))
# It's creating a new integer object because the result of r + 1 is a different immutable value. Then it rebinds x to that object.
# simple terms ,integers are immutable so python cannot update the existing integer object incase of a change of value but creates a new integer object for r+1

