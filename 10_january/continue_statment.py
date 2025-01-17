animal = ["cat","dog","rose","lion","tiger"]
new = []

for i in animal:
    if i == "rose":
        continue
    else:
        print("This is animal :", i)

new.append("rose")
print("This is flower :", new)