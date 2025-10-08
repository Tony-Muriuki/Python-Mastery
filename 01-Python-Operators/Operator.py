#!/usr/bin/python3
# ----------------------------------------------------
# Python Program: Conditional Logic Examples
# ----------------------------------------------------

# Part 1: Club Entry Check
age = 20             # Person's age
has_id = True        # Does the person have an ID card?

# Print variable values
print("Age:", age)
print("Has ID:", has_id)

# Conditional logic to determine access
if age >= 18 and has_id:
    print("✅ Access granted! You are allowed to enter.")
elif age >= 18 and not has_id:
    print("⚠️ Sorry, you need to show your ID to enter.")
else:
    print("❌ Access denied! You must be at least 18 years old.")

# Separator for clarity
print("\n---\n")

# Part 2: Meaning Check
meaning = 2      # Assign a number to the variable 'meaning'

# Conditional logic to check the value
# if meaning > 10:
#     print("Right On")
# else:
#     print("Not Today")

# Ternary Operator Operation
print("Right On!") if meaning > 10 else print("Not today")

# End of program
print("\nProgram finished successfully.")
