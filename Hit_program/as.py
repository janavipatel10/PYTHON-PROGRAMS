import re

pattern = re.compile(r'\d+')  # Compile a regular expression to match one or more digits
match = pattern.search("The number is 12345")

if match:
    print(f"Found number: {match.group()}")
else:
    print("No match found")
