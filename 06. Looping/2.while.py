# Using while loop we can combine with an else if you’d like to:

# EXAMPLE 1
x = 0;
while x < 5:
	print(f'the current value of x is {x}')
	x = x + 1
else:
	print("X is not less than 5")


# EXAMPLE 2
# while loop + break, continue, pass - add additional functionality for various cases.
# break: breaks out the current closest enclosing loop.

x = 0;
while x < 10:
	if x == 5:
		break
	print(f'the current value of x is {x}')
	x = x + 1


# EXAMPLE 3

# example 3.1
number = 100
while number > 0:
        print(number)
        number //= 2

# example 3.2
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)
