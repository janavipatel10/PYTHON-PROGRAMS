test_str = input("insert the string: ")

# printing original string
print("The original string is : " + test_str)

# Convert Snake case to Pascal 
res = test_str.replace("_", " ").title().replace(" ", "")

print("The String after changing case : " + str(res)) 
