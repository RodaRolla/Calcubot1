#!python
#-*-coding: utf-8-*-

# Возвращает короткий список команд
def shortHelp():
	return "/help, /calc, формула=, "

# Читает файл botHelp.txt и возвращает его содержимое	
def longHelp():
	return ''.join(open('help.txt',encoding='utf-8'))