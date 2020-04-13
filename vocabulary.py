import sys

mass = []

class Vocabulary:
	def __init__(self, word, string):
		self._word = word
		self._string = string
		
	def show(self):
		print(self._word, "-", self._string)


def find():
	
		
def main():	
	print("Выберите действие:\n")
	print("1. Занести новое слово в словарь")
	print("2. Поиск по словарю")
	print("3. Показать все")
	print("4. Выйти")
	
	ans = int(input())
	
	if (ans == 1):
		new_word = input()
		new_string = input()
		
		new_voc = Vocabulary(new_word, new_string)
		
		new_voc.show()
		mass.append(new_voc)
			
	elif (ans == 2):
		find()
		
	elif (ans == 3):
		for voc_element in mass:
			voc_element.show()
			
	elif (ans == 4):
		sys.exit(0)
		
	else:
		print("Неправильный номер действия")
	
while(1):	
	main()	
	
	
