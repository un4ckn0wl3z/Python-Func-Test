### Anuwat Khonchuai
### IT 431 / ID 357402360273 
name = input("Enter your name >> ")

def findStringMatching(name):
	pattern = ['P','Y','T','H','O','N']
	for i in range(0,len(name)):
		for j in range(0,len(pattern)):
			if name[i] == pattern[j]:
				print("Found")
				exit(0)


findStringMatching(name)
