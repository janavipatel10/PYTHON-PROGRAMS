class marks:
  Eng = 40
  Urdu = 55
  Math = 60

Marks = marks() 

print('a = ',Marks.Eng)
print('b = ',Marks.Urdu)
print('c = ',Marks.Math)

delattr(marks, 'Math')

print('--After deleting Math attribute--')
print('a = ',Marks.Eng)
print('b = ',Marks.Urdu)

# Raises Error
print('c = ',Marks.Math)