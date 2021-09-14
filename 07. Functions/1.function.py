# DEFINING A FUNCTION

# EXAMPLE 1 
def greeting(name):
  print("Hello " + name)

greeting("Alain")


# EXAMPLE 2 - ARGUMENTS
def greet(first_name, last_name):  # parameter: is the input that you define for your function
  print(f"Hi {first_name} {last_name}")
  print("Welcome aboard")

greet("Alain", "Afonso")            # argument: is the actual value for a giver parameter
greet("Fernando", "Ecumbi")  


# EXAMPLE 3 - default parameter NAME
def greeting(name="NAME"):
  print("Hello " + name)

greeting()


# EXAMPLE 4 - adding
def adding(num1, num2):
  return num1 + num2

adding(10,20)


# EXAMPLE 5 - Checking if the word 'dog' is in the string
# A)
def check(mystring):
  if 'dog' in mystring.lower():
    return True
  else:
    return False

check("My dog ran way")

# B) 
def check(mystring):
  return 'dog' in mystring.lower()


# EXAMPLE 6 - PIG LATIN – transform a normal word into a secret code word
def pig_latin(word):
  first_letter = word[0]

  if first_letter in 'aeiou':
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
  
  return pig_word

pig_latin("apple")
pig_latin("water")


# EXAMPLE 7 - DEFAULT ARGUMENTS: making the "by" an optional parameters

def increment(number, by=1):
  return number + by

print(increment(2, 5))