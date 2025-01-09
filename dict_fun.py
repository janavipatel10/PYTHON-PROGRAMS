person_info = {
    "name": "Alice",
    "age": 30,
    "city": "Los Angeles"
}

# Loop through the dictionary to get key-value pairs
counter = 0
for key, value in person_info.items():
    counter += 1
    print(counter)  
    if counter == 2:  # Print the second key-value pair
        print(f"{key}: {value}")
        break    #