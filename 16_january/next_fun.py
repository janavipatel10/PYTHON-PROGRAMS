#use to next function

fruits = ["apple","banana","cherry","mango"]
iterator  = iter(fruits)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator , "kiwi"))