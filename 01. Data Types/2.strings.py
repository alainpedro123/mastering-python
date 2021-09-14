course = "Python Programming"

# 1) STRING METHODS
print(len(course))  			 # Getting the length of the string
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())  			 # removing the white space of the string
print(course.lstrip())  		 # removing the white space of the string / left side
print(course.rstrip())  		 # removing the white space of the string / right side
print(course.find("Pro"))  		 # finding the index of pro
print(course.replace("P", "j"))  # replace "p" with "j"
print("Pro" in course)  		 # checking for existance
print("Swift" not in course)  	 # checking for existance


# 2) STRING INDEXING AND SLICING
print(course[0])   				# Getting the character at index 0
print(course[5])   				# Getting the character at index 5
print(course[-1])  				# printing the last character of the string
print(course[0:3])  			# Printing the characters from index 0 to 3
print(course[:3])  				# Printing the characters from index 0 to 3
print(course[0:])				# Printing the characters starting from index 0 all the way till the end
print(course[:])   				# printing the whole string
print(course[::])   			# printing the whole string
print(course[::2])   			# it returns this: "Pto rgamn"
print(course[::-1])				# printing the whole string in the reverse order: "gnimmargorP nohtyP"


# 3) CONCATENATION
# EXAMPLE 1 
name = "Alain"
last_letters = name[1:]
combination = 'P' + last_letters
print(combination)  # Plain

# EXAMPLE 2
part_1 = "Hello there"
part_2 = " it's beautiful outside"
final = part_1 + part_2
print(final)  # Hello there it's beutiful outside


# EXAMPLE 3
letter = 'z'
z_10_times = letter * 10
print(z_10_times)

# EXAMPLE 4
number = '2' + '3'
print(number)

# EXAMPLE 5
string = "Hello World"
my_list = string.split()  # converting a STRING into a LIST => ['Hello', 'World']

string_2 = "Hi this is a string"
my_list_2 = string_2.split('i')  # => ['H', ' th', 's ', 's a str', 'ng']


# 4) FORMATED STRING => .format() and f=strings
# EXAMPLE 1
firstName = "Alain"
lastName = " Pedro"
fullName = f"{firstName}{lastName}"
print(fullName)  # Alain Pedro

# EXAMPLE 2
string = "My first name is {}".format('Alain')
print(string)  # My first name is Alain

# EXAMPLE 3
string = "My father {} {} {}".format("is", "very", "clever")
print(string)  # My father is very clever

# EXAMPLE 4
string = "My father {2} {2} {2}".format("is", "very", "clever")
print(string)  # My father clever clever clever

# EXAMPLE 5
string = "My father {i} {v} {c}".format(i="is", v="very", c="clever")
print(string)  # My father is very clever

# EXAMPLE 6
result = 100/777
print("The result is {}".format(result))			# The result is 0.1287001287001287
print(f"The result is {result}")					# The result is 0.1287001287001287
print("The result is {r}".format(r=result))			# The result is 0.1287001287001287
print("The result is {r:1.3f}".format(r=result))    # The result is 0.129

# 5) ESCAPE SEQUENCES
# \ - escape character      \" - escape sequence
#  \'    \\    \n - new line

course_2 = "Python \"Programming"
print(course_2)

course_3 = "Python \'Programming"
print(course_3)

course_4 = "Python \\Programming"
print(course_4)

course_5 = "Python \nProgramming"
print(course_5)