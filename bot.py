#!python
#-*-coding: utf-8-*-

from jopajopa import superCalculator
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import re

def doQu(str):
	str=str.lower()
	if u'ку' in str:
		return u'хай'
	else:
		return u'не понял'

def think(ls):
	return ''.join(ls)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text))
	
def calc(bot, update, args):
	line=''.join(args) # это строка без пробелов
	out=''
	r=re.match('(.+)=',line)
	if r!=None:
		line=r.group(1)
		try:
			out=str(superCalculator(line))
		except Exception as e:
			out="Ошибка вычисления: %s" % e.args
	else:
		out='айяйяй'
	bot.send_message(chat_id=update.message.chat_id, text="%s, it is %s = %s " % (update.message.from_user.first_name, line, out))
		

def xyecho(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text))
	#firstN=update.message.from_user.first_name
	#lastN=update.message.from_user.last_name
	#bot.send_message(chat_id=update.message.chat_id, text="Dear %s %s. You have said fucking %s" % (firstN, lastN))
	
if __name__ == '__main__':
	
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	updater = Updater(token='764096237:AAFJCh0TuxxjJ47peMMjpOTCVp4S-aGJcG0',
						request_kwargs={'proxy_url':'socks5://phobos.public.opennetwork.cc:1090',  'urllib3_proxy_kwargs': {'username': '257314152', 'password': 'cWH5NtTJ'}}) 
	print("Create updater")
	start_handler = CommandHandler('start', start)
	calc_handler = CommandHandler('calc', calc, pass_args=True)
	print("Create command handler")
	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(calc_handler)
	print("Start filters")
	echo_handler = MessageHandler(Filters.text, xyecho)
	updater.dispatcher.add_handler(echo_handler)
	print("Start polling")
	updater.start_polling()
	print("Idle")
	updater.idle()

