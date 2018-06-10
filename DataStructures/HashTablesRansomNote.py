from datetime import datetime

m, n = [int(i) for i in input().split()]
magazine = input().split()
note = input().split()
bnote = note

# def checkMagazine(magazine, note):

# 	for w in note:
# 		if w not in magazine:
# 			return 'No'
# 		else:
# 			magazine.remove(w)

# 	return 'Yes'


#better performance:
def checkMagazine(magazine, note):
	dictNote = {}
	dictMagazine = {}

	for w in note:

		if w not in dictNote:
			dictNote[w] = 1
		else:
			dictNote[w] += 1

	for w in magazine:
		if w not in dictMagazine:
			dictMagazine[w] = 1
		else:
			dictMagazine[w] += 1

	for w in note:
		if(dictNote[w]>dictMagazine[w]):
			return 'No'

	return 'Yes'


startTime = datetime.now()
print(checkMagazine(magazine, note))
print(datetime.now() - startTime)