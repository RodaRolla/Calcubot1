#!/usr/bin/python3
#-*-coding: utf-8-*-

#import re

# Стек для вычислений. Здесь лежат числа
numStack=[]

def equality():
	print()
	
def multiplying():
	global numStack
	numStack.append(numStack.pop()*numStack.pop())

def addition():
	global numStack
	right=numStack.pop()
	left=numStack.pop()
	numStack.append(left+right)
	print("Add %d+%d=%d" % (left,right,numStack[-1]))

def subtraction():
	global numStack
	right=numStack.pop()
	left=numStack.pop()
	numStack.append(left-right)
	print("Sub %d-%d=%d" % (left,right,numStack[-1]))

def division():
	global numStack
	try:
		right=numStack.pop()
		left=numStack.pop()
		numStack.append(left/right)
	except ZeroDivisionError:
		print('T_T')
		raise Exception("Ошибка выполнения. Деление на ноль для %d/%d" % (left,right))
func={
	'+': addition,
	'-': subtraction,
	'*': multiplying,
	'/': division,
	'=': equality
}
	
def isNumber(ls):
	for c in ls:
		if c not in '0123456789.':
			break
	else:
		return True
	return False
	 
def isFunc(ls):
	if ''.join(ls) in func:
		return True
	return False
	
# Ищем границу между токенами
# Если надо рубить токен - ложь
# Иначе истина
def isSame(left,right):
	if left == []:
		return False	# bug!
	if isNumber(left):
		if isNumber(right):
			return True
		return False
	if isFunc(left):
		return False
		
# или число или фнкция
def parseTokens(ls):
	out=[]
	tk=[]
	for symbol in ls:
		print("symbol=%s" % symbol)
		if isSame(tk,symbol):
			tk.append(symbol)
			print("Same! symbol '%s' -> %s" % (symbol,tk))
		else:
			if tk!=[]:
				out.append(''.join(tk))
				print("Out=%s" % out)
			tk=[symbol]
			print("Symbol '%s' => %s" % (symbol,tk))
	if tk!=[]:
		out.append(''.join(tk))
	print(out)
	return out
		
def infixToPostfix(ls):
	stack=[]
	out=[]
	
	for token in ls:
		if isNumber(token):
			out.append(int(token))
			print(out)
		elif isFunc(token):
			if stack==[]:
				stack.append(token)
			else:
				out.append(stack.pop())
				stack.append(token)
		else:
			print("Unknows token '%s'" % token)
			raise Exception("Синтаксическая ошибка. Неопознанный токен '%s'" % token)
		
		# число -> в аут
		# оператор - в стек
	# из стека операторы в ат
	for op in stack[::-1]:
		out.append(op)
	print("Postfix=%s" % out)
	return out

def doToken(token):
	global numStack
	if isinstance(token,int):
		numStack.append(token)
	else:
		if token in func:
			func[token]()
		else:
			print("Syntax error with '%s'" % token) # throw exeption!
			raise Exception("Синтаксическая ошибка в '%s'" % token)

def superCalculator(str):
	global numStack
	for token in infixToPostfix(parseTokens(str)):
		print(token)
		doToken(token)
	result=numStack[-1]
	numStack=[]
	return result

if __name__ == "__main__":
	while True:
		result=superCalculator(input("Code: "))
		print("Result=%d" % result)
		str=input("Text = ")
		

	








