MyAwesomeTupleone = (1, 2, 3, 4, 5)
MyAwesomeTupletwo = (1, 2, 3, 4)
print(MyAwesomeTupleone) # (1, 2, 3, 4, 5)
print(MyAwesomeTupletwo) # (1, 2, 3, 4)
print(type(MyAwesomeTupleone)) # <class 'tuple'>
print(type(MyAwesomeTupletwo)) # <class 'tuple'>

# Tuple Indexing
print(MyAwesomeTupleone[0]) # 1
print(MyAwesomeTupleone[1]) # 2
print(MyAwesomeTupleone[-2]) # 4

# Tuple assing values
MyAwesomeTuplethree = (1, 2, 3, 4, 5)
# MyAwesomeTuplethree[0] = 10 # TypeError: 'tuple' object does not support item assignment

#Tuple Items
MyAwesomeTuplefour = ("Haleem", 1, 2, 3, 4, True)
print(MyAwesomeTuplefour[1]) # 1
print(MyAwesomeTuplefour[0]) # "Haleem"
print(MyAwesomeTuplefour[-1]) # True

# Tuple with one element
MyAwesomeTuplefive = (1,)
print(MyAwesomeTuplefive) # (1,)
print(type(MyAwesomeTuplefive)) # <class 'tuple'>

# Tuple concatenation
MyAwesomeTuplesix = (1, 2, 3)
MyAwesomeTupleseven = (4, 5, 6)
MyAwesomeTupleeight = MyAwesomeTuplesix + MyAwesomeTupleseven
print(MyAwesomeTupleeight) # (1, 2, 3, 4, 5, 6)

# Tuple, list, string Repeat (*)
MyAwesomeTuplenine = (1, 2, 3)
MyAwesomeTupleten = MyAwesomeTuplenine * 3
print(MyAwesomeTupleten) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
MyAwesomeTupleten = ("Hello",) * 3
print(MyAwesomeTupleten) # ('Hello', 'Hello', 'Hello')

# Methods => count()
a = (1, 2, 3, 4, 5, 1, 2, 3)
print(a.count(1)) # 2
print(a.count(2)) # 2
print(a.count(3)) # 2

# Methods => index()
c = (1, 2, 3, 4, 5, 1, 2, 3)
print(c.index(1)) # 0
print(c.index(2)) # 1
print("The Position of index is: {:d}".format(c.index(3))) # The Position of index is: 2

# Tuple Destruct
MyAwesomeTupleeleven = (1, 2, 4, 3)
a, b,_, c = MyAwesomeTupleeleven
print(a) # 1
print(b) # 2    
print(c) # 3

# Home work
Myname = ("Haleem",)
print(Myname) # ("Haleem",)
print(type(Myname)) # <class 'tuple'>

friends = ("Osama", "Ahmed", "Sayed")
friends = ("elzero",) + friends[1:]
print(friends)
print(type(friends))
print(len(friends))

nums = (1, 2, 3)
letters = ("A", "B", "C")
Theall = nums + letters
print(Theall) # (1, 2, 3, 'A', 'B', 'C')
print(len(Theall)) # 6

my_tuple = (1, 2, 3, 4)
a, b, _, d = my_tuple
print(a) # 1
print(b) # 2    
print(d) # 4
