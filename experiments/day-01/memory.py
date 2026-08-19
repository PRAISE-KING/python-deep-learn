# <---------    What exactly is an object in Python, and what does an object contain?   --------->

# The foundation of Python is that Everything is an object.
# Strings.
# Lists.
# Functions.
# Classes.
# Modules.
# Even integers.

# mutable objects - are objects that can be updated /python doesnt create a new object incase of a chsange 
# they include (lists, sets, dictionary)

# immutable objects - cannot be updated instead python creates new objects incase of a change e.g x=5 then x=18...ans will be 18 but the first integer object still exists
# they include (integers, strings, tuples, bool, float)

# EXAMPLE 1
x = 5
# here x is a reference point to the integer object with a value of 5

print(x)
print(id(x))
print(type(x))


# EXAMPLE 2
x = 10
y = x
# here x and y share the same integer object only the reference names are different (x and y)meaning they will have the same id/address as they share same object hence same destination
# 

print(x)
print(y)
print(type(x))
print(type(y))
print(id(x))
print(id(y))


# EXAMPLE 3
p = 10
r = p
p = 17

print(p)
print(r)
print(id(p))
print(id(r))
# from this the p once shared the integer object but then changed to 17 leading to python creating a new object integer with same reference (p)
# now the first object integer remains held with r
# in this case will have different ids for p and r
# all this is because integers are immutable

# EXAMPLE 4
q = [2]
s = q

q.append(8)

print(id(q))
print(id(s))
# since lists are mutable the list object can be updated so no need to creat a new object
# will have same id


# EXAMPLE 5
a = 1000
b = 1000

print(id(a))
print(id(b))
# in this case they will have same identity because python just created one integer object of value 1000 and two reference names (a and b)


# EXAMPLE 6



# # Why this matters for AI

# Suppose your AI loads a 5 GB model.
# If Python copied it every time you passed it to a function...
# 💥 Your computer would run out of memory.
# Instead,
# everything references the same object until a real copy is needed.
# This is one reason Python can work efficiently with large models and datasets.


# This concept is foundational for AI engineering.
# Imagine a neural network:
# model = NeuralNetwork()
# trainer = model
# Are we copying a 500MB model?
# No.
# Both names reference the same object.
# Understanding this prevents memory bugs, accidental data modification, and weird behavior in large AI systems.
# Your mental model is improving. The next concept we attack is:
# "What exactly is an object in Python, and what does an object contain?"
#  Because once you understand that, classes, OOP, PyTorch tensors, FastAPI models, and basically the whole Python ecosystem start making sense.



