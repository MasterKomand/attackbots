#3д тексты

title_programm = """
░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗░░░░░░██████╗░░█████╗░████████╗░██████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝░░░░░░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░█████╗██████╦╝██║░░██║░░░██║░░░╚█████╗░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░╚════╝██╔══██╗██║░░██║░░░██║░░░░╚═══██╗
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗░░░░░░██████╦╝╚█████╔╝░░░██║░░░██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░
"""

error_title = """
███████╗██████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""

#для очищения консоли

import os
try:
    from platform import platform
except:
    try:
        os.system("pip install platform")
    except:
        os.system("pip3 install platform")
    from platform import platform
puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

#функции

def title():
    os.system(delet)
    print(title_programm)

#импорты библиотек

from javascript import require, On
import time

title()
print('Загрузка..')

#подключение

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
GoalFollow = pathfinder.goals.GoalFollow

#создание ботов

title()
print('Сделано командой: HackerRullerTools')
time.sleep(3)

def start():
    title()
    version = input('Выберите версию майнкрафта: ')
    title()
    print('1: Один бот\n1: Два бота\n1: Три бота\n')
    try:
        test_menu = int(input('Выберите кол-во ботов: '))
    except:
        error('Вы сделали не правильный выбор!')
    finally:
        if test_menu <= 0 or test_menu >= 4:
            error('Вы сделали не правильный выбор!')
        else:
            title()
            ip = input('Напишите айпи: ')
            ip2 = ''
            test = False
            port2 = ''
            for i in ip:
                if i == ':':
                    test = True
                else:
                    if test == False:
                        ip2 = ip2 + i
                    else:
                        port2 = f'{port2}{i}'
                        port2 = int(port2)
            return_data = (test_menu, ip2, port2, version)
            return return_data

def error(text):
    os.system(delet)
    print(error_title)
    print(text)
    time.sleep(3)
    start()

#начало создания

data = start()
ip = data[1]
port = data[2]
test_menu = data[0]
version = data[3]

#создание и запуск ботов

if test_menu >= 1:
    title()
    if test_menu == 1:
        print('Пожалуйста введите никнэйм для бота!\n')
    else:
        print('Пожалуйста введите никнэймы для ботов!\n')
    #запрос данных первого бота
    username1 = input('Никнэйм первого бота: ')
    #запуск бота
    bot1 = mineflayer.createBot({
        'host':ip,
        'port':port,
        'username':f'{username1}',
        'version':version})
if test_menu >= 2:
    #запрос данных второго бота
    username2 = input('Никнэйм второго бота: ')
    #запуск второго бота
    bot2 = mineflayer.createBot({
        'host':ip,
        'port':port,
        'username':f'{username2}',
        'version':version})
if test_menu >= 3:
    #запрос данных третьего бота
    username3 = input('Никнэйм третьего бота: ')
    #запуск третьего бота
    bot3 = mineflayer.createBot({
        'host':ip,
        'port':port,
        'username':f'{username3}',
        'version':version})
title()
nick = input('Введите никнэйм игрока на которого нужно напасть: ')

title()

def test_cooldown():
    try:
        cooldown = int(input('Интервал между ударами в секундах: '))
        return cooldown
    except:
        error('Интервал должен быть числом!')

cooldown = test_cooldown()

#проверки
title()
print('Консоль:\n')
if test_menu >= 1:
    mcData1 = require('minecraft-data')(bot1.version)
    movements1 = pathfinder.Movements(bot1, mcData1)
    @On(bot1, 'kicked')
    def kicked1(this, reason, test, *args):
        print(f'Первый бот кикнут причина: {reason}!')
    @On(bot3, 'spawn')
    def spawned1(*args):
        print(f'Первый бот зашел!')
    @On(bot1, 'respawn')
    def respawned1(*args):
        print('Первый бот умер!')

if test_menu >= 2:
    mcData2 = require('minecraft-data')(bot2.version)
    movements2 = pathfinder.Movements(bot2, mcData2)
    @On(bot2, 'kicked')
    def kicked2(this, reason, test, *args):
        print(f'Второй бот кикнут причина: {reason}!')
    @On(bot2, 'spawn')
    def spawned2(*args):
        print(f'Второй бот зашел!')
    @On(bot2, 'respawn')
    def respawned2(*args):
        print('Второй бот умер!')

if test_menu >= 3:
    mcData3 = require('minecraft-data')(bot3.version)
    movements3 = pathfinder.Movements(bot3, mcData3)
    @On(bot3, 'kicked')
    def kicked3(this, reason, test, *args):
        print(f'Третий бот кикнут причина: {reason}!')
    @On(bot3, 'spawn')
    def spawned3(*args):
        print(f'Третий бот зашел!')
    @On(bot3, 'respawn')
    def respawned3(*args):
        print('Третий бот умер!')

#наводка

time.sleep(3)

if test_menu >= 1:
    bot1.loadPlugin(pathfinder.pathfinder)
    player1 = bot1.players[nick]
    target = player1.entity
    bot1.pathfinder.setMovements(movements1)
    goal = GoalFollow(target, 1)
if test_menu >= 2:
    bot2.loadPlugin(pathfinder.pathfinder)
    bot2.pathfinder.setMovements(movements2)
if test_menu >= 3:
    bot3.loadPlugin(pathfinder.pathfinder)
    bot3.pathfinder.setMovements(movements3)

while True:
    try:
        if test_menu >= 1:
            bot1.pathfinder.setGoal(goal, True)
            bot1.attack(target)
        if test_menu >= 2:
            bot2.pathfinder.setGoal(goal, True)
            bot2.attack(target)
        if test_menu >= 3:
            bot3.pathfinder.setGoal(goal, True)
            bot3.attack(target)
    finally:
        time.sleep(cooldown)