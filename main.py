import smtplib
import psycopg2
import telebot
from telebot import types
from string import Template




smtpObj=smtplib.SMTP('smtp.yandex.ru',587)
smtpObj.starttls()
smtpObj.login('dimage.59@ya.ru','')

bot = telebot.TeleBot(config.token_api)