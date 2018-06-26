statement = "make hay while the sun shines"
for x in statement:
    print("current letter",x)
    if x == "e":
        break

for x in statement:
    if x == "e":
        break
    print("current letter",x)
for x in statement:
    if x == "w":
        continue
    print("current letter",x)
    
