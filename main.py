someArray = ["1", "", "hhh", "kjkkfj", "fhfhfh"]

newArrayOfStringsTreeOrLess = []
for el in someArray:
    if len(el) <= 3:
        newArrayOfStringsTreeOrLess.append(el)

print(newArrayOfStringsTreeOrLess)