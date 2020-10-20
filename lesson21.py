# # def test_1():
# # 	print('Python Program to Make a Simple Calculator_files')
# # test_1()	


# # def test2():
# # 	print(' set a hacker')
# # test2()

# def name_1(name, lastname):
# 	print(name+"  "+lastname)
# name_1 ("Gag", "Yedigaryan")


# def name_1(name1, name2):
# 	print("thr youngest ichild is  " +name1)
# name_1 (name1="Emil",name2 = "john")



# def my_funktion(coyntry = 'Armenia'):
# 	print('if i am form ' + coyntry)


# def a()	:
# 	pass
# # my_funktion('swedian')
# my_funktion('INDIA')
# my_funktion()
# 	pass

# def my_funktion(food):
	# for x in food:
		# print(x)
# fruits = ['apple','banana','cherry']
# my_funktion(fruits)	


# def my_fun(**kwargs):	
# 	print(kwargs)
# my_fun(a ='serie',c = 'psi')
# '	print(10 * x)

# c = my_funktion(3)	
# print(c)

# add = lambda x,y: x+y
# print(add(2,5))


def add(x,y):
	return x+y



def minus (x,y):
	return x-y
 


def multiplay (x,y):
	return x*y


def divison(x,y):
	return x/y
	

def result():
	num1 = int(input('create number 1   '))
	num2 = int(input ('create number2   '))
	choice = input('+ - / *')
	if choice == '+':
		print(add (num1,num2))
	elif choice == '-':
		print(minus(num1,num2))
	elif choice == '*':
		print(multiplay(num1,num2))
	elif choice == '/':
		print(divison(num1,num2))	
result()