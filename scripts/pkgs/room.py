from datetime import date
from random import choice
from random import randint


class Room:

    def __init__(self):
        self.today = date.today()

    def get_name(self):
        return 'Dungeon Room'

    def create(self):
        print("This room's theme is: " + self.get_theme())

        if randint(0, 1):
            print('This room has an Item!')

        if randint(0, 1):
            print('This room has an Inhabitant!')

        if randint(0, 1):
            print('This room has an Faction!')
        return None

    def get_theme(self):
        themes = []
        with open('scripts/themes.data') as file:
            themes = [line.rstrip() for line in file]

        if self.get_week() == 1:
            return str(themes[0])
        else:
            return str(themes[self.get_week() - 1])

    def get_week(self):
        return int(date(self.today.year, self.today.month, self.today.day).strftime("%U"))

    def get_template_path(self):
        return '/templates/Dungeon/room.md'

    def get_day_to_schedule(self):
        num = self.today.day - 1

        if num >= len(self.schedule):
            tmp_num = num
            while tmp_num >= len(self.schedule):
                tmp_num -= len(self.schedule)

            return self.schedule[tmp_num]
        else:
            return self.schedule[num]

    def get_file_path(self):
        return '/Dungeon/Level_' + str(f'{self.today.month:02}') + '/Room_' + str(f'{self.today.day:02}') + '.md'

    def get_file_dir(self):
        return '/Dungeon/Level_' + str(f'{self.today.month:02}')
