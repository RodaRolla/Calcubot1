#!python
#-*-coding: utf-8-*-

from jopajopa import superCalculator
from fileObj import createobj, findobj
from botHelp import *
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import re

adminID=[]

def think(ls):
	return ''.join(ls)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text))


def help(bot,update):
	try:
		bot.send_message(chat_id=update.message.chat_id, text=longHelp())
	except Exception as e:
		bot.send_message(chat_id=update.message.chat_id, text="Ошибка чтения файла подсказки:\n%s" % e.args)
	
def calc(bot, update, args):
	line=''.join(args) # это строка без пробелов
	out=''
	# что-то
	bot.send_message(chat_id=update.message.chat_id, text="%s, it is %s = %s " % (update.message.from_user.first_name, line, out))

# Если это строка для калькулятора -- возвращаем выражение
# Иначе None
def isCalc(s):
	r=re.match('(.+)=',s)
	if r!=None:
		return ''.join(r.group(1).split(' '))
	return None

def isQu(s):
	if u'ку' in s.lower():
		return True
	return False

def doQu(s,n):
	return u'хай %s' % n

def xyecho(bot, update):
	if isCalc(update.message.text):
		try:
			line=isCalc(update.message.text)
			out="%s = %d" % (line,superCalculator(line))
		except Exception as e:
			out="Ошибка вычисления: %s" % e.args
		bot.send_message(chat_id=update.message.chat_id, text=out)
		return
	#if isQu(update.message.text):
	#	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text, update.message.from_user.first_name))
	#	return 
	r=re.match('\scоздать\sбиблиотеку:\s+(.+)', update.message.text, re.IGNORECASE)
	if r!=None:
		bot.send_message(chat_id=update.message.chat_id, text=createobj(update.message.from_user.id, r.group(1)))
		return
	r=re.match('\s*посмотреть\sбиблиотеку:\s+(.+)', update.message.text, re.IGNORECASE)
	if r!=None:
		bot.send_message(chat_id=update.message.chat_id, text=findobj(update.message.from_user.id, r.group(1)))
		return
	bot.send_message(chat_id=update.message.chat_id, text="Не понял\nЯ понимаю лишь %s" % shortHelp())
	
	
if __name__ == '__main__':
	
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	updater = Updater(token='764096237:AAFJCh0TuxxjJ47peMMjpOTCVp4S-aGJcG0',
						request_kwargs={'proxy_url':'socks5://phobos.public.opennetwork.cc:1090',  'urllib3_proxy_kwargs': {'username': '257314152', 'password': 'cWH5NtTJ'}}) 
	print("Create updater")
	start_handler = CommandHandler('start', start)
	calc_handler = CommandHandler('calc', calc, pass_args=True)
	help_handler = CommandHandler('help', help)
	print("Create command handler")
	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(calc_handler)
	updater.dispatcher.add_handler(help_handler)
	print("Start filters")
	echo_handler = MessageHandler(Filters.text, xyecho)
	updater.dispatcher.add_handler(echo_handler)
	print("Start polling")
	updater.start_polling()
	print("Idle")
	updater.idle()


