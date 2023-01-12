from datetime import date
from datetime import datetime
from os import path
from shutil import copy
from random import randint


def get_week():
    return int(date(TODAY.year, TODAY.month, TODAY.day).strftime("%U"))


def create_room():

    template_file = path.dirname(path.realpath(__file__)) + '/templates/dungeon.md'

    if path.exists(template_file):
        new_room = 'Dungeon/Level ' + str(TODAY.month) + '/Room_' + str(DAY) + '.md'
        copy(template_file, new_room)


def get_themes():
    with open('scripts/themes.data') as file:
        return [line.rstrip() for line in file]


def get_theme():
    if WEEK == 1:
        return THEMES[0]
    else:
        return THEMES[WEEK-1]

START_DATE = datetime.strptime('01/01/23', "%m/%d/%y")
TODAY = date.today()
DAY = TODAY.day
WEEK = get_week()
THEMES = get_themes()

print('------------------')
print('| Todays room is |')
print('------------------')
print('Level ' + str(TODAY.month) + ' Room_' + str(DAY) )
create_room()
print('\n')
print('---------------')
print('| SUGGESTIONS |')
print('---------------')

print("This room's theme is: " + str(get_theme()))

if randint(0, 1):
    print('This room has an Item!')

if randint(0, 1):
    print('This room has an Inhabitant!')

if randint(0, 1):
    print('This room has an Faction!')
