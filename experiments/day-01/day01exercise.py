
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Level 1 (Warm-up)  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 1
x = 100

y = x

print(x)
print(y)

print(id(x))
print(id(y))

# Questions:

# Are the IDs the same?
        # yes ids are the same
# Why?
        # both x and y refer to the same integer object


# Exercise 2
x = "Python"

y = x

x = "AI"

print(x)
print(y)

print(id(x))
print(id(y))

# Draw memory before and after reassignment.
        # before : both x and y refer to the same str object as shown in the diagram below.
        
            # x --- str object ---> value("Python")
            #           |
            #           y
            
        # After : x is assigned to new string object and therefore rebinds to the new string object created by python as shown below.

            # y ---> str object ---> value("Python")
            # x ---> str object ---> value("AI")          - new str object


# Exercise 3
a = [1, 2]

b = a

a.append(3)

print(a)
print(b)

print(id(a))
print(id(b))

# Did Python create another list?
        # no it didn't
# why?
        # a and b both refer to the same list object and with list being mutable python didnt create another list object but instead updated the existing one 
        # this also means they both have the same id
        
        
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Level 2  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 4
a = [1, 2]

b = a

a = [5, 6]

print(a)
print(b)

# Memory diagram before and after with explanation.
        # before : both a and b refer to the same list object
        
            # a -- list object --> value ([1, 2])
            #           |
            #           b
        
        # after : a gets reassigned and so python creates a new list object and rebinds a
        
            # b ---> list object ---> value([1, 2])
            # a ---> list object ---> value([5, 6])       - new list object 
            
            
# Exercise 5
name = "Praise"

print(id(name))

name = name + " King"

print(id(name))

# will id be same or different?
        # different
# Why?
        # the id will differ because str object is immutable and so python created and rebinded the new str object to name
        
        
# Exercise 6
x = [1]

y = x

z = y

z.append(2)

print(x)
print(y)
print(z)

# How many list objects exist?
        # one
# why?
        # x and y refer to the same list object and with z = y means z refer to the same list object as y and since list object is mutable the z.append(2) updates the existing list object.
        
        

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Level 3  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 7
a = [10]

b = a

c = [10]

print(id(a))
print(id(b))
print(id(c))

# Questions:

# Which IDs match?
        # a and b
# Why?
        # a and b refer to the same list object
        
        
# Exercise 8
a = [1, 2]

b = a

c = b

a.append(100)

print(a)
print(b)
print(c)

# Draw memory.
        # before :
                #               c
                #               |
                # a --- list object ---> value ([1, 2])
                #               |
                #               b
        
        # after :
                #               c
                #               |
                # a --- list object ---> value ([1, 2, 100])
                #               |
                #               b
        
        
# Exercise 9
x = 5

y = x

z = y

x = 10

print(x)
print(y)
print(z)

# How many integer objects exist at the end?
        # two 
# why?
        # because at first x y and z refered to the same integer object with value of 5, but x was later reassigned to new integer object with value of 10 and hence rebinds to the new integer object 



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Level 4  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 10
numbers = [1, 2]

other = numbers

numbers = numbers + [3]

print(numbers)
print(other)

# This is a trap.

# Does

numbers + [3]

# modify the list?
# Or create another one?
        # it creates another list object
# Explain.
        # Think of it like this.
        # Old list [1,2]
        # New list [1,2,3]
        # Then
        # numbers =
        # rebinds numbers to that new list.
        # Memory becomes
        # other
        #  │
        #  ▼
        # [1,2]
        # numbers
        #  │
        #  ▼
        # [1,2,3]
        # Therefore
        # print(numbers)
        # ↓
        # [1,2,3]
        # print(other)
        # ↓
        # [1,2]
        # This distinction is very important.
        
        
# Exercise 11
numbers = [1, 2]

other = numbers

numbers += [3]

print(numbers)
print(other)

# Looks almost identical.
# Completely different internally.

# Explain.
        # Internally,
        # lists implement __iadd__()
        # which means In-place addition.
        # So instead of creating another list, Python modifies the existing object.
        # Memory
        # Before :
        
        # numbers ─┐
        #          │
        # other ───┘
        # [1,2]
        
        # After :
        # numbers ─┐
        #          │
        # other ───┘
        # [1,2,3]

        # Same object.
        # Same id.
        # This difference between + and += is something experienced Python developers rely on.


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Level 5  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Exercise 12
a = []

b = a

c = b

d = c

d.append(1)

print(a)
print(b)
print(c)
print(d)

# How many names?
        # 4 names
# How many list objects?
        # 1 list objects 
        # because all the four names refer to the same list object
        
        
# Exercise 13
a = []

b = a

c = []

print(id(a))
print(id(b))
print(id(c))

# Memory diagram.
        # Python creates
        # List A []
        # and binds a .Then b points to List A.
        # After
        # c = []
        # Python creates List B []
        # Memory
        # List A
        # []
        # ▲
        # │
        # a
        # │
        # b

        # List B
        # []
        # ▲
        # │
        # c

        # Two list objects.
        # Different ids.
        # Same value.


# Level 6 (Senior Engineer)
# Exercise 14

# Predict every step.

x = [1, 2]
        # python creates a list object with value of [1, 2] with reference name as x
y = x
        # new reference name y is created refering to the same list object as x
x.append(3)
        # the list object is modified through reference name r
x = [100]
        # x gets reassigned and python creates a new list object and rebinds x to it
y.append(4)
        # list object referenced by y is modified with new value appended to it
print(x)
        # prints the output of the list object referenced by x
print(y)
        # prints the output of the list object referenced by y

                # Memory
                # Initially
                # x
                # │
                # ▼
                # [1,2]

                # y
                # │
                # └───────┘

                # After
                # x.append(3)
                # [1,2,3]

                # shared.
                # Then

                # x=[100]
                # y ───► [1,2,3]
                # x ───► [100]

                # Then

                # y.append(4)
                # y ───► [1,2,3,4]
                # x ───► [100]

                # Output
                # [100]
                # [1,2,3,4]


# Exercise 15
a = "AI"

b = a

c = b

a = "Machine"

b = "Learning"

print(a)

print(b)

print(c)

# How many string objects exist at the end?
        # 3 string objects


        
# Final Boss

# No computer.

# Paper only.

a = [1]

b = a

c = b

a.append(2)

b = [10]

c.append(3)

a = [100]

print(a)

print(b)

print(c)

# I want

# every memory state
# every reassignment
# every object created
# final output        
        
        
        
        
        