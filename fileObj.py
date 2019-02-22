#!python
#-*-coding: utf-8-*-

import os
import re

libraryFolder='lib'

def isNameValid(name):
	return None!=re.match('[0-9a-z_]+$',name)

def libFileName(id,name):
	return 'lib/'+id+'-'+name+'.txt'

# Проверяет на наличие файла 
def findobj(id,s):
	if not isNameValid(s):
		return 'Используй 0-9 a-z и _'
	if os.path.exists(libFileName(id,s)):
		return 'такая библиотека существует!'
	return 'Такой библиотеки не существует'

# создает файл или удаляет уже существующий
def createobj(id,s):
	if not isNameValid(s):
		return 'Используй 0-9 a-z и _'
	try:
		file = open(libFileName(id,s), 'w', encoding='utf-8')
		file.close()
		return "Готово!"
	except Exception as e:
		return e.args
		
# пишет строку в файл
def writeObj(id,s,text):
	pass

# читает последние 5 строк
def readObj(id,s):
	pass
	
if __name__ == '__main__':
	cmd={
		'c': createobj,
		'f': findobj
		}
	while True:
		line=input('Команда {c,f,w,r} id name [text]: ')
		(command,id,name,text)=line.split(' ')
		if command == 'w':
			print(cmd[command](id,name,text))
		else:
			print(cmd[command](id,name))