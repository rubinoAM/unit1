vowels = "aeiouAEIOU"
numVow = 0
vSet = set(vowels)
rendWord = []
inpWord = raw_input("Please input a word. Try a word with double vowels! ")

for i in inpWord:
	if(i in vSet):
		numVow += 1
		rendWord.append(i)
		if(numVow == 2):
			rendWord.append((i)*3)
	else:
		numVow = 0
		rendWord.append(i)
		
wordRendered = "".join(rendWord)
print (wordRendered)