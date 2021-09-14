import math		# module

# 1) NUMBERS
x = 1           # integer
x = 1.1         # float
x = 1 + 2j      # complex number: a + bi

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)   # floating point number
print(10 // 3)  # getting an integer number
print(10 % 3)   # getting the remainder of a division
print(10 ** 3)  # left to the power of right 10^3 = 1000

x = 10
x = x + 3
x += 3

# 2) FUNCTIONS TO WORK WITH NUMBERS

print(round(2.9))   # it's equal 3
print(round(abs(-2.9)))   # it's equal 3
print(math.ceil(3.2))  # it's equal to 4 using "import math"

# 3) INPUT
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")