#!/usr/bin/python3

# ----------------------------------------------------
# Simple Python program demonstrating conditional logic
# ----------------------------------------------------

# Define two variables
age = 20
has_id = True  # This represents if the person has an ID card

# Print variable values for clarity
print("Age:", age)
print("Has ID:", has_id)

# Conditional logic using if, elif, and else
# This block checks if a person is allowed to enter a club.
if age >= 18 and has_id:
    # Both conditions must be True: age is 18+ AND person has an ID
    print(" Access granted! You are allowed to enter.")
elif age >= 18 and not has_id:
    # Age is enough, but no ID
    print(" Sorry, you need to show your ID to enter.")
else:
    # If neither of the above is true, person is underage
    print(" Access denied! You must be at least 18 years old.")

# End of program
print("Program finished successfully.")
