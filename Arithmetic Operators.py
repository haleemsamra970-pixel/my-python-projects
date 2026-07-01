#------- Arithmetic Operators -------#

# [1] Addition (+)
print(10 + 50) # =>60
print(20.9 + 9.1) # => 30.0
print(-65 + 87) # => 22

# [2] Subtraction (-)
print(20 - 9) # => 11
print(55- 60) # => -5
print(-99.8 - 7) # => -106.8

# [3] Multiplication (*)
print(7 * 9)


#-----List-----#

myAwesomeList = ["one" , "tow" , "1" , "py" , "Hand" , True]

print(myAwesomeList) #whole List
print(myAwesomeList[1]) #tow
print(myAwesomeList[-1]) #True
print(myAwesomeList[3]) #py

print(myAwesomeList[0:3]) # 'one' , 'tow' , '1'
print(myAwesomeList[:3]) # 'one' , 'tow' , '1'
print(myAwesomeList[1:]) # 'tow' , '1' , 'py' , 'Hand' , 'True'

print(myAwesomeList[::1]) # ["one" , "tow" , "1" , "py" , "Hand" , True]
print(myAwesomeList[::2]) # 'one' , '1' , 'Hand'

print(myAwesomeList) # ["one" , "tow" , "1" , "py" , "Hand" , True]
myAwesomeList[1] = 2
myAwesomeList[-1] = False
print(myAwesomeList) # ["one" , "2" , "1" , "py" , "Hand" , False]

myAwesomeList[0:2] = []
print(myAwesomeList) # ['1', 'py', 'Hand', False]

# append()
myfriends = ["Adam" , "Malek" , "Abood"]
myoldfriends = ['karam', 'mohammed', 'salem']
myfriends.append("Adel")
myfriends.append("Omar")
myfriends.append("Ali")
myfriends.append(myoldfriends)
print(myfriends) # ['Adam', 'Malek', 'Abood', 'Adel', 'Omar', 'Ali', ['karam', 'mohammed', 'salem']]

print(myfriends[2]) # => Abood
print(myfriends[3]) # => Adel
print(myfriends[0]) # => Adam
print(myfriends[4]) # => Omer
print(myfriends[6][0]) # => karam

# extend()

a = [1 , 2 , 3 , 4]
b = ["A" , "B" , "C"]
c = ["one" , "two"]
a.extend(b)
print(a) # [1, 2, 3, 4, 'A', 'B', 'C']
a.extend(c)
print(a) # [1, 2, 3, 4, 'A', 'B', 'C', 'one', 'two']

# remove()
x = [1, 2, 3, 4, "Haleem", 8, "python", "Haleem"]
x.remove("Haleem")
print(x) # [1, 2, 3, 4, 8, 'python', 'Haleem']

# sort()
w = [20, 10, 30, 11, 24, -19]
w.sort()
print(w) # [-19, 10, 11, 20, 24, 30]
w.sort(reverse=True)
print(w) # [30, 24, 20, 11, 10, -19]
r = ['A' , 'B' , 'C']
r.sort(reverse=True)
print(r) # ['C', 'B', 'A']

# reverse()
u = [1 ,2 ,3 ,4 ,5]
u.reverse()
print(u) # [5, 4, 3, 2, 1]

# clear()
v = [1, 2, 3, 4, 5]
v.clear()
print(v) # []

# copy()
m = [1, 2, 3, 4, 5]
c = m.copy()
print(m) # [1, 2, 3, 4, 5]
print(c) # [1, 2, 3, 4, 5]

m.append(6)
print(m) # [1, 2, 3, 4, 5, 6]
print(c) # [1, 2, 3, 4, 5]

# count()
n = [1, 2, 3, 4, 5, 1, 2, 1]
print(n.count(1)) # 3

# index()
print(n.index(2)) # 1
print(n.index(1)) # 0

# insert()
p = [1, 2, 3, 4, 5] 
p.insert(0, "haleem")
print(p) # ['haleem', 1, 2, 3, 4, 5]
p.insert(-1, "python")
print(p) # ['haleem', 1, 2, 3, 4, 'python', 5]

# pop()
q = [1, 2, 3, 4, 5]
print(q.pop(4)) # 5

# myhomework

myfriends = ["Adam" , "Malek" , "Abood" , "Adel" , "Omar" , "Ali"]
print(myfriends[0]) # => Adam
print(myfriends.pop(0)) # => Adam
print(myfriends[-1]) # => Ali
print(myfriends.pop(-1)) # => 
myfriends = ["Adam", "Malek", "Abood", "Adel", "Omar", "Ali"]

print(myfriends[::2])   # الأسماء الفردية
print(myfriends[1::2])  # الأسماء الزوجية

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4]) # => ['Ahmed', 'Sayed', 'Ali']
print(friends[0: :4]) # => ['Osama', 'Mahmoud']
print(friends[3:5]) # => ['Ali', 'Mahmoud']

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3] = "Elzero"
friends[4] = "Elzero"
print(friends) # => ['Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero']

Friends = ["Osama", "Ahmed", "Sayed"]
Friends.append("Ali")
print(Friends) # => ['Osama', 'Ahmed', 'Sayed', 'Ali']
Friends.insert(0, "Mahmoud")
print(Friends) # => ['Mahmoud', 'Osama', 'Ahmed', 'Sayed', 'Ali']

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
del friends[0:2]
print(friends) # => ['Sayed', 'Ali', 'Mahmoud']
friends.pop()
print(friends) # => ['Sayed', 'Ali']

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school) 
print(friends) # => ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort(reverse=False)
print(friends) # => ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
friends.sort(reverse=True)
print(friends) # => ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends)) # => 6

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0]) # => Django
print(technologies[-1][-1]) # => Web