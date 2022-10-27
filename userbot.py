# Author: SAURUX
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.errors.exceptions.forbidden_403 import UserPrivacyRestricted
from pyrogram.errors.exceptions.bad_request_400 import UserBot
from pyrogram.errors.exceptions.bad_request_400 import UserChannelsTooMuch
from pyrogram.errors.exceptions.bad_request_400 import UserIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import UserNotMutualContact
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied
from pyrogram.errors.exceptions.bad_request_400 import UserKicked


from pyrogram.types import ChatPermissions
import pathlib

import time
from time import sleep
import random

from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram import types

app = Client("my_account")

directory = str(pathlib.Path(__file__).parent.absolute())


# Массовое добавление людей на канал
@app.on_message(filters.command("add", prefixes=".") & filters.me)
def addUsers(_, message):
	channel = message.text.split("@")[1]
	chat_id = message.chat.id
	chat_name = message.chat.username

	message.delete()
	i = 0

	for member in app.iter_chat_members(chat_id):
		try:
			if(i >= 50):
				break
			if(member.user.is_bot == False):
				app.add_chat_members(channel, member.user.id)
				i = i + 1
				sleep(0.15)
		except FloodWait as e:
			time.sleep(e.x)
		except UserPrivacyRestricted:
			pass
		except UserBot:
			pass
		except UserChannelsTooMuch:
			pass
		except UserIdInvalid:
			pass
		except UserNotMutualContact:
			pass
		except ChatAdminRequired:
			pass
		except UsernameNotOccupied:
			pass
		except UserKicked:
			pass


@app.on_message(filters.command("adder", prefixes=".") & filters.me)
def addUsers(_, message):
	from_channel = message.text.split(".adder ")[1].split("@")[1]
	channel = message.text.split(" ")[1].split("@")[1]
	from_id = app.get_chat(from_channel).id

	message.delete()

	for member in app.iter_chat_members(from_id):
		try:
			app.add_chat_members(channel, member.user.id)
			sleep(0.05)
		except FloodWait as e:
			time.sleep(e.x)
		except UserPrivacyRestricted:
			pass
		except UserBot:
			pass
		except UserChannelsTooMuch:
			pass
		except UserIdInvalid:
			pass
		except UserNotMutualContact:
			pass


# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▌"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) # 50 ms

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

# - Красивая анимация текста
@app.on_message(filters.command("out", prefixes=".") & filters.me)
def out(_, msg):
	origin = msg.text.split(".out ", maxsplit=1)[1] # 
	texts = origin
	to_print = texts
	output = ""

	for x in range(len(origin) * int(5)): # 5 loops
		try:
			output = to_print[1:] + to_print[0] 
			msg.edit(output)
			to_print = output 
			sleep(0.08)
		except FloodWait as e:
			sleep(e.x)


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):

	try:
		user = msg.chat
		perc = 0
		curr = " <a href='tg://user?id=%s'" % user.id + ">"+user.first_name+"</a>"

		while(perc < 100):
			try:
				text = "👮‍ Взлом"+curr+" в процессе " + str(perc) + "%"
				msg.edit(text)

				perc += random.randint(1, 3)
				sleep(0.1)

			except FloodWait as e:
				sleep(e.x)

		msg.edit("🟢 "+user.first_name+" успешно взломан!")
		sleep(2)

		msg.edit("👽 Поиск секретных порнографии...")
		perc = 0

		while(perc < 100):
			try:
				text = "👽 Поиск секретных порнографии " + str(perc) + "%"
				msg.edit(text)

				perc += random.randint(1, 5)
				sleep(0.15)

			except FloodWait as e:
				sleep(e.x)

		msg.edit("😎 Пользователь:"+curr+"\n❤️ Найдено: "+random.randint(2,1000)+" порнографии!")
	except TypeError:
		user = msg.reply_to_message.from_user
		perc = 0
		curr = " <a href='tg://user?id=%s'" % user.id + ">"+user.first_name+"</a>"

		while(perc < 100):
			try:
				text = "👮‍ Взлом"+curr+" в процессе " + str(perc) + "%"
				msg.edit(text)

				perc += random.randint(1, 3)
				sleep(0.1)

			except FloodWait as e:
				sleep(e.x)

		msg.edit("🟢 "+user.first_name+" успешно взломан!")
		sleep(2)

		msg.edit("👽 Поиск секретных порнографии...")
		perc = 0

		while(perc < 100):
			try:
				text = "👽 Поиск секретных порнографии " + str(perc) + "%"
				msg.edit(text)

				perc += random.randint(1, 5)
				sleep(0.15)

			except FloodWait as e:
				sleep(e.x)

		msg.edit("😎 Пользователь:"+curr+"\n❤️ Найдено: "+str(random.randint(2,1000))+" порнографии!")

# - Спамер (формат: -текст -кольво -задержка)
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam_message(_, message):
	message.delete()
	text = message.text.split("-")
	delay = float(text[3])
	for i in range(int(text[2])):
		message.reply_text(text[1])
		sleep(delay)

# - Массовая рассылка
@app.on_message(filters.command("mass", prefixes=".") & filters.me)
def mass(_, message):
	chat_id = message.chat.id
	msg = message.text.split(".mass ", maxsplit=1)
	text = msg[1]
	message.delete()

	for member in app.iter_chat_members(chat_id):
		try:
			app.send_message(member.user.id, text)
			sleep(0.05)
		except FloodWait as e:
			time.sleep(e.x)

@app.on_message(filters.command("ment", prefixes=".") & filters.me)
def mass(_, message):
	chat_id = message.chat.id
	chat_name = message.chat.username
	msg = message.text.split(".ment ", maxsplit=1)
	text = msg[1]
	message.delete()

	for member in app.iter_chat_members(chat_id):
		try:
			app.send_message(chat_id, text + " <a href='tg://user?id=%s'" % member.user.id + ">ᅠ</a>", parse_mode="html")
			sleep(0.05)
		except FloodWait as e:
			time.sleep(e.x)

	print("[+] Mention Mode Done!")

# - Информация
@app.on_message(filters.command("info", prefixes=".") & filters.me)
def Information(_, message):
	message.delete()

	# markup = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Клонировать пользователя", callback_data="clone")]])

	try:
		count_photos = app.get_profile_photos_count(message.chat.id)
		photos = app.get_profile_photos(message.chat.id)
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		username = message.chat.username
		id = message.chat.id

		app.send_message(message.chat.id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"📀 Имя: "+first_name+"\n💿 Фамилия: "+last_name+"\n✍🏻 Username: @"+username+"\n❕ CHAT ID: " + str(id))

	except TypeError:
		try:
			count_photos = app.get_profile_photos_count(message.chat.id)
			photos = app.get_profile_photos(message.chat.id)
			first_name = message.chat.first_name
			username = message.chat.username
			id = message.chat.id

			app.send_message(id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"\n📀 Имя: "+first_name+"\n💿 Фамилия: ⭕️"+"\n✍🏻 Username: @"+username+"\n❕ CHAT ID: " + str(id))

		except TypeError:
			try:
				count_photos = app.get_profile_photos_count(message.chat.id)
				photos = app.get_profile_photos(message.chat.id)
				first_name = message.chat.first_name
				id = message.chat.id

				app.send_message(id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"\n📀 Имя: "+first_name+"\n💿 Фамилия: ⭕️"+"\n✍🏻 Username: ⭕️"+"\n❕ CHAT ID: " + str(id))

			except TypeError:
				try:
					count_photos = app.get_profile_photos_count(message.reply_to_message.from_user.id)
					photos = app.get_profile_photos(message.reply_to_message.from_user.id)
					first_name = message.reply_to_message.from_user.first_name
					last_name = message.reply_to_message.from_user.last_name
					username = message.reply_to_message.from_user.username
					id = message.reply_to_message.from_user.id

					app.send_message(message.chat.id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"\n📀 Имя: "+first_name+"\n💿 Фамилия: "+last_name+"\n✍🏻 Username: @"+username+"\n❕ CHAT ID: " + str(id))
				except TypeError:
					try:
						count_photos = app.get_profile_photos_count(message.reply_to_message.from_user.id)
						photos = app.get_profile_photos(message.reply_to_message.from_user.id)
						first_name = message.reply_to_message.from_user.first_name
						username = message.reply_to_message.from_user.username
						id = message.reply_to_message.from_user.id

						app.send_message(message.chat.id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"\n📀 Имя: "+first_name+"\n💿 Фамилия: ⭕️"+"\n✍🏻 Username: @"+username+"\n❕ CHAT ID: " + str(id))
					except TypeError:
						count_photos = app.get_profile_photos_count(message.reply_to_message.from_user.id)
						photos = app.get_profile_photos(message.reply_to_message.from_user.id)
						first_name = message.reply_to_message.from_user.first_name
						id = message.reply_to_message.from_user.id

						app.send_message(message.chat.id, "👤 Пользователь\n🤳🏽 Аватарки: "+str(count_photos)+"\n📀 Имя: "+first_name+"\n💿 Фамилия: ⭕️"+"\n✍🏻 Username: ⭕️"+"\n❕ CHAT ID: " + str(id))


app.run()