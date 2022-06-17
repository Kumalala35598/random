import config
import telebot
from random import randint


bot = telebot.TeleBot(config.TOKEN)
Try = 1
secretNum = 0
inGame = False

@bot.message_handler(commands=["start"])
def start(message):
	text = "Привет, "+str(message.from_user.first_name)+"!\n Чтобы начать игру, нажми /game"
	bot.send_message(message.chat.id, text)
@bot.message_handler(commands=["game"])
def game(message):
	global secretNum, inGame
	secretNum  = randint(1,100)
	inGame = True
	bot.send_message(message.chat.id, 'Я загадал число от 1 до 100 - угадай его!')
@bot.message_handler(func = lambda message: message.text.isdigit()==True and inGame==True)
def game(message):
	global secretNum,inGame,Try
	usernum = int(message.text)
	if usernum > secretNum:
		Try += 1
		bot.send_message(message.chat.id, 'Моё число меньше')
	elif usernum < secretNum:
		Try += 1
		bot.send_message(message.chat.id, 'Моё число больше')
	elif usernum == secretNum:
		bot.send_message(message.chat.id, 'Ты угадал')
		bot.send_message(message.chat.id, 'Тебе потребовалось '+str(Try) + 'попытки(-ок)')
		inGame = False
		Try = 1	
if __name__ == '__main__':
	bot.infinity_polling()