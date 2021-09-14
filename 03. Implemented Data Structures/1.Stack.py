##### 13. STACKS
# Last In First OUT

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

last = stack.pop()
print(last)
print(stack)

print(stack[-1])  # getting the item on top of the stack

# checking if the stack is empty
if not stack:  # that means we have an empty stack
    # do something