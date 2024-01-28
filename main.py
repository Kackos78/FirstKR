someArray = ["111", "22", "sdffs", "kjkkfj", "fhfhfh"]

newArrayOfStringsTreeOrLess = []
for el in someArray:
    if len(el) <= 3:
        newArrayOfStringsTreeOrLess.append(el)

print(newArrayOfStringsTreeOrLess)