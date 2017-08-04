

li2 = []
li3 = []
strFinalString2 = ''
with open("a.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)


l= ""
for i in range(0, len(array)):  # ekar
	j= str(array[i])
	l="'"+j+","

	print l.lstrip()
'''

l= ""
for item in range(1,30):
	item=str(item)
	l="'"+item+"'"+","

	print l.lstrip()
'''