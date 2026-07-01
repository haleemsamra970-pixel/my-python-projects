# [1] Set Items Are Enclosed in Curly Braces
from os import name


myset = {"Haleem", "Osama", "Ahmed", "Sayed"}
print(myset) # {'Haleem', 'Osama', 'Ahmed', 'Sayed'} # {'Osama', 'Ahmed', 'Sayed', 'Haleem'}
 
 # [2] Set Items Are not ordered And Not Indexed
 #print(myset[0]) # gives an error

 # [3] Set Indexing and Slicing cannot be done
 #print(myset[0:2]) # gives an error

 # [4] Set Items Are Unique
myset = {"Haleem", "Osama", "Ahmed", "Sayed", "Haleem"}
print(myset) # {'Haleem', 'Osama', 'Ahmed', 'Sayed'} # {'Osama', 'Ahmed', 'Sayed', 'Haleem'}

# Methods

#clear()
myset = {"Haleem", "Osama", "Ahmed", "Sayed"}
myset.clear()
print(myset) # set() # {}

# union()
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
set3 = {9, 10}
print(set1.union(set2, set3)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# add()
num1 = {1, 2, 3}
num1.add(4)
num1.add(5)
print(num1) # {1, 2, 3, 4, 5}

# copy()
num2 = {1, 2, 3}
num3 = num2.copy()
print(num3) # {1, 2, 3}
num2.add(4)
print(num3) # {1, 2, 3} # num3 is not affected by the change in num2

# discard()
num4 = {1, 2, 3, 4, 5}
num4.discard(3)
print(num4) # {1, 2, 4, 5}
num4.discard(6) # does not give an error if the item is not found
print(num4) # {1, 2, 4, 5}

# update()
num5 = {1, 2, 3}
num6 = {4, 5, 6}
num5.update(["Hello", "World"])
num5.update(num6)
print(num5) # {1, 2, 3, 4, 5, 6, 'Hello', 'World'}

#difference()
num7 = {1, 2, 3, 4, 5}
num8 = {4, 5, 6, 7, 8}
print(num7.difference(num8)) # {1, 2, 3} # items that are in num7 but not in num8
print(num8.difference(num7)) # {6, 7, 8} # items that are in num8 but not in num7

# difference_update()
num9 = {1, 2, 3, 4, 5}
num10 = {1, 2, 3, "haleem", "osama"}
num9.difference_update(num10)
print(num9) # {4, 5} # items that are in num9 but not in num10
num10.difference_update(num9)
print(num10) # {1, 2, 3, "haleem", "osama"} # items that are in num10 but not in num9

# intersection()
num11 = {1, 2, 3, 4, 5}
num12 = {4, 5, 6, 7, 8}
print(num11.intersection(num12)) # {4, 5} # items that are in both num11 and num12
print(num12.intersection(num11)) # {4, 5} # items that are in both num12 and num11

# intersection_update()
num13 = {1, 2, 3, 4, 5}
num14 = {4, 5, 6, 7, 8}
num13.intersection_update(num14)
print(num13) # {4, 5} # items that are in both num13 and num14

#symmetric_difference()
num15 = {1, 2, 3, 4, 5}
num16 = {4, 5, 6, 7, 8}
print(num15.symmetric_difference(num16)) # {1, 2, 3, 6, 7, 8} # items that are in num15 or num16 but not in both
print(num16.symmetric_difference(num15)) # {1, 2, 3, 6, 7, 8} # items that are in num16 or num15 but not in both

#symmetric_difference_update()
num17 = {1, 2, 3, 4, 5}
num18 = {4, 5, 6, 7, 8}
num17.symmetric_difference_update(num18)
print(num17) # {1, 2, 3, 6, 7, 8} # items that are in num17 or num18 but not in both

# issuperset()
num19 = {1, 2, 3, 4, 5}
num20 = {1, 2, 3}
print(num19.issuperset(num20)) # True # num19 contains all items of num20
print(num20.issuperset(num19)) # False # num20 does not contain all items of num19

# issubset()
num21 = {1, 2, 3}
num22 = {1, 2, 3, 4, 5}
print(num21.issubset(num22)) # True # num21 is a subset of num22
print(num22.issubset(num21)) # False # num22 is not a subset of num21

# isdisjoint()
num23 = {1, 2, 3}
num24 = {4, 5, 6}
num25 = {1, 2, 3, 4, 5}
print(num23.isdisjoint(num24)) # True # num23 and num24 have no items in common
print(num23.isdisjoint(num25)) # False # num23 and num25 have some items in common

# Dictionary Methods
User = {
    "name": "Haleem",
    "age": 25,
    "country": "Egypt",
    "skills": ["Python", "PHP", "JavaScript"],
    "rating": 4.5
}
print(User) # {'name': 'Haleem', 'age': 25, 'country': 'Egypt', 'skills': ['Python', 'PHP', 'JavaScript'], 'rating': 4.5}

# two-dimensional dictionary
Users = {
    "user1": {
        "name": "Haleem",
        "age": 25,
        "country": "Egypt",
        "skills": ["Python", "PHP", "JavaScript"],
        "rating": 4.5
    },
    "user2": {
        "name": "Osama",
        "age": 30,
        "country": "Saudi Arabia",
        "skills": ["Python", "PHP", "JavaScript"],
        "rating": 4.7
    }
}
print(Users) # {'user1': {'name': 'Haleem', 'age': 25, 'country': 'Egypt', 'skills': ['Python', 'PHP', 'JavaScript'], 'rating': 4.5}, 'user2': {'name': 'Osama', 'age': 30, 'country': 'Saudi Arabia', 'skills': ['Python', 'PHP', 'JavaScript'], 'rating': 4.7}}
print(Users["user1"]) # {'name': 'Haleem', 'age': 25, 'country': 'Egypt', 'skills': ['Python', 'PHP', 'JavaScript'], 'rating': 4.5}
print(Users["user1"]["name"]) # Haleem
print(Users["user2"]["skills"]) # ['Python', 'PHP', 'JavaScript']

# clear()
user1 = {
    "name": "Haleem"
}
print(user1) # {'name': 'Haleem'}
user1.clear() 
print(user1) # {} # empty dictionary

# update()
user2 = {
    "name": "Osama",
}
user2.update({"age": 30})
print(user2) # {'name': 'Osama', 'age': 30}

# copy()
user3 = {
    "name": "Ahmed",
    "age": 28
}
user4 = user3.copy()
print(user4) # {'name': 'Ahmed', 'age': 28}
user3.update({"country": "Egypt"})
print(user3) # {'name': 'Ahmed', 'age': 28, 'country': 'Egypt'}
print(user4) # {'name': 'Ahmed', 'age': 28} # user4 is not affected by the change in user3

# keys() + values()
print(user3.keys()) # dict_keys(['name', 'age', 'country'])
print(user3.values()) # dict_values(['Ahmed', 28, 'Egypt'])

# setdefault()
user5 = {
    "name": "Sayed",
    "age": 35
}
user5.setdefault("country", "Egypt")
print(user5) # {'name': 'Sayed', 'age': 35, 'country': 'Egypt'}
user5.setdefault("age", 40) # does not change the value of age because it already exists
print(user5) # {'name': 'Sayed', 'age': 35, 'country': 'Egypt'}

# Popitem()
user6 = {
    "name": "Haleem",
    "age": 25,
    "country": "Egypt"
}
print(user6) # {'name': 'Haleem', 'age': 25, 'country': 'Egypt'}
user6.update({"skills": ["Python", "PHP", "JavaScript"]})
print(user6.popitem()) # ('skills', ['Python', 'PHP', 'JavaScript']) # removes the last item added to the dictionary
print(user6) # {'name': 'Haleem', 'age': 25, 'country': 'Egypt'}

# items()
user7 = {
    "name": "Osama",
    "age": 30,
    "country": "Saudi Arabia"
}

allitems = user7.items()
print(user7) # {'name': 'Osama', 'age': 30, 'country': 'Saudi Arabia'}
user7.update({"skills": ["Python", "PHP", "JavaScript"]})
print(allitems) # dict_items([('name', 'Osama'), ('age', 30), ('country', 'Saudi Arabia'), ('skills', ['Python', 'PHP', 'JavaScript'])]) # allitems is updated because it is a view 

# fromkeys()
a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X"
print(dict.fromkeys(a, b)) # {'MyKeyOne': 'X', 'MyKeyTwo': 'X', 'MyKeyThree': 'X'} # creates a new dictionary with keys from a and values from b

print('='*50)

# Home Work
 
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = [1, 2, 3, 4, 5]
print(unique_list) 
print(type(unique_list)) 
del unique_list[4]
print(unique_list)

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters)) # {1, 2, 3, 'A', 'B', 'C'}
nums.update(letters)
print(nums) # {1, 2, 3, 'A', 'B', 'C'}
nums.add("A")
nums.add("B")
nums.add("C")
print(nums) # {1, 2, 3, 'A', 'B', 'C'} # adds the elements as individual elements to the set nums

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set) # set() # {} # clears the set my_set
my_set.update("A", "B")
print(my_set) # {'A', 'B'} # adds the elements as individual elements to the set my_set

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two)) # True # set_one is a subset of set_two
print(set_two.issubset(set_one)) # False # set_two is not a subset of set_one

a = {"HTML Progress Is:": "0%"}
print(a)
c = {"CSS Progress Is": "0%"}
d = {"JavaScript Progress Is": "0%"}
print(c)
print(d)