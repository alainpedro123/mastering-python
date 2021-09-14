# 1) NUMBER - Integer
students_count = 1000

# 2) NUMBER - Float
students_count = 4.99

# 3) BOOLEAN
is_published = False
is_published = True
1 == 1	# True
1 > 2	# False

# 4) STRING
full_name = "Alain Afonso"

print('Hello World')
print('Hello \nWorld')
print('Hello \tWorld')


# 5) METHODS
x = 3.5, y = 3
int(x)      # 3
float(y)    # 3.0
bool(y)     # True
str()



# 6) SWAPPING VARIABLES

# First Way 
x = 10
y = 11
print("x: ", x, "y: ", y)

z = x
x = y
y = z
print("x: ", x, "y: ", y)

# Second way  - by using tuples
a, b = 10, 11
print("a: ", a, "b: ", b)

a, b = b, a
print("a: ", a, "b: ", b)