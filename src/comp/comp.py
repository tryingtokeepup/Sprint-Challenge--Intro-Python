# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# Holy Jesus Batman, this took a while to write.
a = [Human.name for Human in humans if Human.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [Human.name for Human in humans if Human.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.


# def letter_range(start, stop):
#     for x in map(chr, range(*map(ord, ['a', 'h'])))
#     yield chr(c)

# x in map((chr, range(*map(ord, ['C', 'G'])))
# guess mapping over might be ... overly complicated
print("Starts between C and G, inclusive:")
# this is SO CAVEMAN. I don't like it.
c = [Human.name for Human in humans if Human.name[0] in ['C', 'D', 'E', 'F', 'G']]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [Human.age + 10 for Human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# we can concat, we can join, but maybe if we simply use f`string` we will be fine
e = [f"{Human.name}-{Human.age}" for Human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(Human.name, Human.age)
     for Human in humans if Human.age >= 27 and Human.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.

# I wonder if this requires a map like Javscript so that we don't modify the original humans list.
# oh wow, okay. So to do this, we need to take the original Human tuple, and then rebuild the stuff inside it with the changes done to the original data. This was confusing.
# what the test expects:  expected = [Human("ALICE", 34), Human("BOB", 37), Human("CHARLIE", 42), Human("DAPHNE", 35), Human("EVE", 31), Human("FRANK", 23), Human("GLENN", 47), Human("HARRISON", 17), Human("IGON", 46), Human("DAVID", 36)]

print("All names capitalized:")
g = [Human(newHuman.name.upper(), newHuman.age + 5) for newHuman in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
# helper function = for x in range(2, (int)(math.sqrt(n))+1)

print("Square root of ages:")
h = [math.sqrt(Human.age) for Human in humans]
print(h)
