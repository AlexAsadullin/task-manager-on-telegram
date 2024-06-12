import json # для сохранения задач
import datetime # для работы со временем
from time import sleep # для задержки
import telebot  # для работы с ботом

TOKEN = '7175712627:AAEnewR_LaPlruldxttUpbT5GpnvDH1_duA'
bot = telebot.TeleBot(TOKEN) # обратились к боту по токену

with open("message.txt", "r") as file:
    MESSAGE = json.loads(file.read()) # считали id чата пользователя

while True: # бесконечный цикл прогоняется раз 60 секунд
    with open("tasks.txt", "r") as file:
        tasks = json.loads(file.read()) # считали задачи пользователя
    now = datetime.datetime.now()
    current_time = now.strftime("%H.%M") # считали текущее время: часы и минуты
    new_tasks = tasks.copy()
    for key, value in tasks.items(): # проходимся по всем задачам из словаря
        hour, minut = value.split('.')
        current_hour, current_min = current_time.split('.')
        if current_hour == hour and current_min == minut:
            bot.send_message(MESSAGE['chat_id'], f'hey! Dont forget to {key} at {value}') # напоминаем, если время пришло
            del new_tasks[key] # удаляем задачу, о которой напомнили
            with open("tasks.txt", "w") as file:
                file.write(json.dumps(new_tasks)) # обновили данные
        if '.' not in value:
            del new_tasks[key] # очищаем задачи, где время введено неверно
    sleep(60) # задержка 1 минута
