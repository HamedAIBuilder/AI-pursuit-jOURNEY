# This is our original "Hello World" line. We'll keep it for comparison.
# print("Hello, World!")

# --- NEW STUFF STARTS HERE ---

# 1. Ask the user for their name
# The 'input()' function displays a message and then waits for the user to type something
# and press Enter. Whatever they type is then stored in our 'user_name' variable.
user_name = input("What's your name? ")

# 2. Use the user's name in the greeting
# Now, instead of just "World", we use an f-string (formatted string literal)
# to easily put the content of our 'user_name' variable right into the greeting message.
print(f"Hello, {user_name}! Nice to meet you.")

# --- NEW STUFF ENDS HERE ---