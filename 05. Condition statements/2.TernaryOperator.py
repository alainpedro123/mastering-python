# TERNARY OPERATOR

# Example 1

# without Ternary Operator
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)


# with Ternary Operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)



# Example 2

is_my_friend = False
send_message = "Grant access" if is_my_friend else "Do not grant access!"
print(send_message)