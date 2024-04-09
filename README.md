# task-managet-on-telegram
This task manager saves your task and reminds you about it in time! You always must add a deadline to be more productive. 

used framewoeks and modules: telebot, datetime, os, sqlite3
Global variables: 
1) tasks: list of dictionaries - saves each task as a dict: {'name': 'title', 'time': class datetime}
2) CONST: dict - saves chat id, user id to use it in any function
3) TOKEN: string - unique bot's token for telegram api

Classes:
1) Users: self.id = message.from_user.id, self.username = message.from_user.username, self.chatid = message.chat.id

Functions:
1) def hello: recieves 1st message and saves all info about user: id, username, chatid. Adds new users to DataBase. Creates two buttons: 'Add task' -> def create_task, 'My tasks' -> just shows all users'tasks (in one message separeted with "\n")
2) def create_task: aska user to write title of the task -> def add_time
3) def add_time: ###

Objects:
1) bot: class 
