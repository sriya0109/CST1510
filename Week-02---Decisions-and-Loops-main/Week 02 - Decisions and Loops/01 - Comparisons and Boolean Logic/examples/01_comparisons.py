"""
COMPARISONS
===========
Six operators, one job each: ask a question, get True or False.   Run:  python 01_comparisons.py
"""

# --- 1. The six operators ---------------------------------------------------

value = 23.7
limit = 20

print(value == limit)     # False  - equal to?
print(value != limit)     # True   - not equal to?
print(value >  limit)     # True   - greater than?
print(value <  limit)     # False  - less than?
print(value >= limit)     # True   - greater than or equal to?
print(value <= limit)     # False  - less than or equal to?


# --- 2. The result is always a bool -----------------------------------------

is_over = value > limit

print(is_over)            # True
print(type(is_over))      # <class 'bool'>


# --- 3. = stores, == asks ----------------------------------------------------
# This is the single most common slip this week.

limit = 20          # =  : "limit now holds 20"
print(limit == 20)  # == : "does limit hold 20?"  -> True

# limit = 20 == True and limit == 20 look similar. They are not the same
# operation. Read = as "gets", == as "is this the same as".


# --- 4. Comparing different types -------------------------------------------
# A number and its text version are never equal, no matter what they look like.

print(20 == "20")     # False - int vs str, never equal
print(20 == 20.0)     # True  - int vs float, numbers still compare fairly


# --- TRY IT ------------------------------------------------------------------
# 1. Set attempts = 4 and max_attempts = 3. Print whether attempts is over the max.
# 2. Predict, then check: 90 >= 90   and   90 > 90
# 3. Explain out loud why "3" == 3 is False.
inputs = [4, 3, 90, 90, "3", 3]
attempts = inputs[0]
max_attempts = inputs[1]
print(attempts > max_attempts)  # True
print(inputs[2] >= inputs[3])    # True
print(inputs[2] > inputs[3])     # False
print(inputs[4] == inputs[5])    # False
#as the string "3" is not the same as the integer 3, they are different types and therefore not equal.
print(90 >= 90)  # True
print(90 > 90)   # False
print('"3" == 3 is False because they are different types: one is a string and the other is an integer.')
print('The string "3" represents the character 3, while the integer 3 represents the numeric value 3. Since they are not the same type, they cannot be equal.') 
