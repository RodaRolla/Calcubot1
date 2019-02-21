#!python
#-*-coding: utf-8-*-
from jopajopa import superCalculator
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
def doQu(str):
	if 'qu' in str:
		return u'хай'
	else:
		return u'не понял'
	
def think(ls):
	return ''.join(ls)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text))
	
def calc(bot, update, args):
	bot.send_message(chat_id=update.message.chat_id, text="%s, it is %d " % (update.message.from_user.first_name, superCalculator(''.join(args))))
		

def xyecho(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=doQu(update.message.text))
	
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


