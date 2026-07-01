##Numbers##

#Integer
print(type(1))
print(type(100))
print(type(-100))

#Float
print(type(1.77))
print(type(2.88))
print(type(-100.800))

#Complex
mycomplexnumber = 5+7j
print(type(mycomplexnumber))

print("Real part is: {}".format(mycomplexnumber.real))
print("Imaginary part is: {}".format(mycomplexnumber.imag))

# [1] You can convert from Int to float or complex
# [2] You can convert from float to Int or complex
# [3] You cannot convert coplex to any type

#[1]
print(100)
print(float(100)) # =>100.0
print(complex(100)) # =>(100+0j)

#[2]
print(100.7) 
print(int(100.7)) # =>100
print(complex(100.7)) # =>(100.7+0j)

#[3]
print(100+9j)
print(int(100+9j)) #Error

