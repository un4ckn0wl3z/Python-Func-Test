### Anuwat Khonchuai
### IT 431 / ID 357402360273 

num_reg = int(input("Enter Number of Reg to find Area >> "))
print()
result_list = []
def findRegArea(width,height):
	area = width * height
	return area

for i in range(1,num_reg+1):
	width = int(input("Please Enter width of Reg#%d >> " % i))
	height = int(input("Please Enter height of Reg#%d >> " % i))
	result = findRegArea(width,height)
	result_list.append(result)
	print("-" * 20)

for j in range(0,num_reg):
	print("Area of Reg#%d = %d "%(j+1, result_list[j]))
