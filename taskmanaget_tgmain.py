import telebot
import json
from telebot import types

token = '7175712627:AAEnewR_LaPlruldxttUpbT5GpnvDH1_duA'
bot = telebot.TeleBot(token)


class Task:
    def __init__(self, title):
        self.title = title
        self.comment = None
        self.deadline = None

    def __str__(self):
        return f'{self.title}, выполнить до: {self.deadline}, комментарий: {self.comment}'


tasks = [Task('Rate TaskManager 5* on GitHub')]
const = {}


@bot.message_handler(commands=['start'])
def hello(message):
    const['chat_id'] = message.chat.id
    const['message'] = message
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Add task', callback_data='add'))
    markup.add(types.InlineKeyboardButton('My tasks', callback_data='mine'))
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}! \nWhat are your goals for today?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global const
    if callback.data == 'add':
        msg = bot.send_message(const['chat_id'], 'Enter your task:')
        bot.register_next_step_handler(msg, create_task)

    elif callback.data == 'mine':
        markup = types.InlineKeyboardMarkup()
        for i in range(len(tasks)):
            markup.add(types.InlineKeyboardButton(f'{i+1}) {tasks[i].title}, until {tasks[i].deadline}', callback_data=f'task{i}'))
        bot.send_message(const['chat_id'], text='Your tasks for now:', reply_markup=markup)

    """elif callback.data == 'task0':
        print('i see task 0')"""


def create_task(message):
    global tasks
    title = message.text
    task = Task(title)
    tasks.append(task)

    msg = bot.send_message(const['chat_id'], 'Type the deadline like:\nHOURS.MINUTES.DAY.MONTH.YEAR')
    bot.register_next_step_handler(msg, add_time)


def add_time(message):
    if message.text.count('.') == 4:
        hour, minute, day, month, year = message.text.split('.')
        '''!!!!!!!'''
        # tasks[-1].deadline = deadline
        bot.reply_to(message, 'Task added, well done!')
    else:
        bot.reply_to(message, 'Wrong format! Try again!')
        create_task(message)



bot.enable_save_next_step_handlers(delay=1)
bot.load_next_step_handlers()

bot.infinity_polling()
