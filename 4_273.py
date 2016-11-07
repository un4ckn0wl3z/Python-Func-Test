### Anuwat Khonchuai
### IT 431 / ID 357402360273 

def FindGrade(score):
	if score >= 80 and score <= 100:
		grade = 'A'
	elif score >= 70 and score <= 79:
		grade = 'B'
	elif score >= 60 and score <= 69:
		grade = 'C'
	elif score >= 50 and score <= 59:
		grade = 'D'
	else:
		grade = 'F'

	return grade


std_num = int(input("Enter Student number >> "))
STD_NAME_LIST = []
STD_NAME_GRADE = []
for i in range(1,std_num+1):
	std_name = input("Enter STDNAME #%d >> "%i)
	STD_NAME_LIST.append(std_name)
	std_score = int(input("Enter STDSCORE #%d >> "%i))
	std_grade = FindGrade(std_score)
	STD_NAME_GRADE.append(std_grade)
	print("-"*20)

def printSTDDetail(STD_NAME_LIST, STD_NAME_GRADE):
	for i in range(0,std_num):
		print(STD_NAME_LIST[i] + "'s Grade is " + STD_NAME_GRADE[i])

printSTDDetail(STD_NAME_LIST, STD_NAME_GRADE)
