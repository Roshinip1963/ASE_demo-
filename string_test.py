# check_string.py
import sys
# Direct input here
input_value = 1369# ✅ Change to a number to simulate failure

# Check if it's a string
if isinstance(input_value, str):
    print("Success: Input is a string.")
    exit(0)
else:
    print("Error: Input is not a string.")
    exit(1)
