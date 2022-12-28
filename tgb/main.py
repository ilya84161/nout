# This is a sample Python script. api f694ebae6b249be0190837654e6ea5b10872473d895bd5342d0787a604eaee1e
# api layer WrhIbEPUz0Cj837vbaxjTQodFabC50FR   https://apilayer.com/account

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import telebot
from extensions import ConverterValyut, helping
from config import token_tlg
Token = token_tlg
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help', 'values', 'conv'])
def help_and_list(message: telebot.types.Message):
    if message.text.lower() == '/help' or message.text == '/start':
        bot.reply_to(message, helping)
    elif message.text == '/values':
        s = ConverterValyut.list_valyuta()
        bot.reply_to(message, f'{message.chat.username}, \n {s}')
    elif message.text.split()[0] == '/conv':
        s = ConverterValyut.get_price(message.text.split()[2], message.text.split()[3], message.text.split()[1])
        bot.reply_to(message, s)

@bot.message_handler(content_types=['text', 'voice'])
def privetstvie(message: telebot.types.Message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'Zдорово!')
    else:
        bot.reply_to(message, f'введена неверная команда, проверьте регистр.\n команды пишутся маленькими буквами {helping}')

bot.polling(none_stop=True)