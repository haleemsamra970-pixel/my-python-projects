# =========================
# Numbers In Python
# =========================

# Integer (int)
print(type(1))
print(type(100))
print(type(-100))

# Float
print(type(1.77))
print(type(2.88))
print(type(-100.800))

# Complex
mycomplexnumber = 5 + 7j

print(type(mycomplexnumber))

# Real & Imaginary Parts
print("Real part is: {}".format(mycomplexnumber.real))
print("Imaginary part is: {}".format(mycomplexnumber.imag))


# =========================
# Type Conversion
# =========================

# [1] You can convert from int to float or complex
print(100)
print(float(100))      # 100.0
print(complex(100))    # (100+0j)

# [2] You can convert from float to int or complex
print(100.7)
print(int(100.7))      # 100
print(complex(100.7))  # (100.7+0j)

# [3] You cannot convert complex to int
print(100 + 9j)

# This gives an error
# print(int(100 + 9j))


#Home work

print(type(100))
print(type(100.4))
print(type(100.4 + 0j))

mycomplexnumber = 1 + 2j

print(type(mycomplexnumber))

print("Imaginary part is: {}".format(mycomplexnumber.imag))
print("Real part is: {}".format(mycomplexnumber.real))

mynum = 10
print("{: .10f}".format(mynum))

mynumber = 159.650
print(int(mynumber))

print(100 - 115)