print("I love Python") 
print("I love programming")
print("hallo Python")
if True:
    print("I love Python") # this is inline comment
    print(type(5)) # int => integer

    print(type(100.7)) # float => floating point number
    print(type(1.8799)) # float => floating point number
    print(type(-100.999)) # float => floating point number
    
    print(type("hallo python")) # str => string 
     
    print(type( [1 , 2 , 3 , 4] )) # list
    print(type( (1 , 2 ,3 , 4))) # tuple
    print(type({"one" :1 , "two" :2 , "three" :3})) # dict => dictionary

    print(type(2==7)) # bool => boolean
    print(type(4==4))

    print(9++4) # => 13


    myvarible = "my value"
    print(myvarible) # => my value



    # can start with (a-z) - (A-Z) or Underscore
    # you cannot stat with number or special characters
    # you can include (0-9) or Underscore
    # you cannot Include special characters 
    # Name is not like name [case sensitive]
    

    name = "haleem samra" # single word => normal
    myname = "haleem samra" # two word => camelcase
    my_name = "haleem samra" # two word => snake_case

    print(name)
    print(myname)
    print(my_name)
    

    help("keywords")
    a, b, c = 1, 2, 3

    print(b) # => 2
    print(a) # => 1
    print(c) # => 3

    # Back Space
    print("hallo\bworld") # will remove (o) => \b 

    # Escape new line + \ 
    print("hallo " \
    "I love " \
    "python")


    # Escape Back slash
    print("hallo python \\")

      # Escape Back slash
    print('hallo python\'text') # hallo python 'text'

     # Escape Back slash
    print("hallo python\"text") # hello python "text"

     # Line feed
    print("hallo python\ntext") # but text in the next line => \n

    # carriage return
    print("123456\rABCD") # take the first four letters => \r

    # Horizontal Tab
    print("hallo\tpython") # make a tab => \t

    # character Hex value
    print("\x68")
    print("\x68\x61\x6C\x65\x65\x6D") # \xhh => hex value

    bsd = "I love "
    py = "python"
    print(bsd + py) # => I love python

    a = "hallo\
    hi\
    thanks" # 

    b = "a \
    b \
    c"
    print(a + "\n" + b)


    mystringOne = 'This is single Quote'

    mystringTwo = "This is Double Quotes"
    
    mystringthree = 'This is Double Quotes "Text" '

    print(mystringOne) # => This is single Quote
    print(mystringTwo) # => This is Double Quotes
    print(mystringthree) #=> this is Double Quotes "Text"

    mystringfour = """ first
    second "text" 'text'
    third"""
    
    mystringfive = ''' first
    second 'text' \\ "text"
    third'''
    
    print(mystringfour)
    print(mystringfive)

    mystring = "I love python"

    print(mystring[3]) # Index 3 => o
    print(mystring[8]) # Index 8 => y
    print(mystring[-1]) # Index -1 => first character from End (n)
    print(mystring[-6]) # Index -6 => 6th character from End (p)

    print(mystring[3:7]) # ove
    print(mystring[ :13]) # if start is not here will start from 0
    print(mystring[6: ]) # if end is not here will go to the end
    print(mystring[ : ]) # full data

    print(mystring[ ::1]) # full data
    print(mystring[ ::2]) # => Ilv yhn
    print(mystring[ ::3]) # => Io tn
    print(mystring[ ::4]) # => Ivyn
    
    a = "I love python"
    b = "     I love python     "
    print(len(a)) # => 13 step
    print(len(b)) # => 23 step
 

    # strip() rstrip() lstrip()

    a = "    I love python    "
    print(a.strip())
    print(a.rstrip())
    print(a.lstrip())

    a = "####I love python####"
    print(a.strip("#")) # Remove all (#)
    print(a.rstrip("#")) # just remove the right side 
    print(a.lstrip("#")) # just remove the left side

    a = "@#@#I love python@#@#"
    print(a.strip("@#")) # Remove all
    print(a.rstrip("@#")) # just remove the right side
    print(a.lstrip("@#")) # just remove the left side

    #title()

    b = "I will Play football in The morning"
    print(b.title())

    # capitalize()

    b = "I will Play football in The morning" 
    print(b.capitalize())


    # zfill()
    
    c, d, e, g  = "1", "11", "111", "1111"
    print(c) # =>1 
    print(d) # =>11
    print(e) # =>111
    print(g) # =>1111
    
    print(c.zfill(4)) # => 0001
    print(d.zfill(4)) # => 0011
    print(e.zfill(4)) # => 0111
    print(g.zfill(4)) # => 1111

    # upper()

    g = "haleem" 
    
    print(g.upper()) # => HALEEM

    # lower()

    h = "HALEEM"

    print(h.lower()) # => haleem


    # split()
    
    L = "I love Python and PHP"
    print(L.split()) # => ['I','love','python','and','PHP']

    K = "I-love-Python-and-PHP"
    print(K.split("-")) # => ['I','love','python','and','PHP]

    O = "I-love-Python-and-PHP"
    print(O.split("-", 2)) # => ['I','love','python-and-PHP']

    P = "I-love-Python-and-PHP"
    print(P.split("-", 3)) # => ['I','love','python', 'and-PHP']

    # rsplit()

    O = "I-love-Python-and-PHP"
    print(O.rsplit("-", 2)) # => ['I-love-python','and','PHP']
     
    # center()

    e = "haleem" 
    print(e.center(9)) # spaces 
    print(e.center(9, "#")) # hashes
 
    # count()

    r = "I love python and PHP because PHP is easy"
    print(r.count("PHP")) # 2 PHP
    print(r.count("PHP",0 ,25)) # only 1 PHP

    #swapcase()

    m = "I Love python"
    n = "i lOVE PYTHON"
    print(m.swapcase())
    print(n.swapcase())

    # startswith()

    i = "I love python"
    print(i.startswith("I")) # True
    print(i.startswith("p")) # false
    
    print(i.startswith("p", 7, 12)) # True

    # endswith()
    i = "I love python"
    print(i.endswith("n")) # True
    print(i.endswith("p")) # false
    
    print(i.endswith("e", 0, 6)) # True

    #index(substring, Start, End)

    a = "I love python"
   # print(a.index("p")) # index number 7
   # print(a.index("p", 0, 10)) # index number 7
   # print(a.index("p", 0, 5)) # valueError

    #find(substring, Start, End)

    m = "I love python"
    print(m.find("p")) # index number 7
    print(m.find("p", 0, 10)) # index number 7
    print(m.find("p", 0, 5)) # -1
    
    # rjust(width, fill char) , ljust(width, fill char)

    c = "Haleem"
    print(c.rjust(10))
    print(c.rjust(10,"#"))

    c = "Haleem"
    print(c.ljust(10))
    print(c.ljust(10,"#"))

    # splitlines()

    e = "first line\nsecond line\nthird line"
    print(e.splitlines())

    # expandtabs()

    p = "first line\tsecond line\tthird line"
    print(p.expandtabs(10))

    three = " "
    four = ""
    print(three.isspace())
    print(four.isspace())

    five = "i love python"
    six = "I Love Python"
    print(five.islower())
    print(six.islower())

    # replace(old value, new value, count)

    a = "one one two three four"
    print(a.replace("one" , "1"))
    print(a.replace("two" , "2"))

    # join(Iterable)

    mylist = ["haleem" , "yasser" , "nahed" ]
    print("-".join(mylist))

    # %S => string
    # %d => number
    # %f => Float