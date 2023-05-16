from datetime import date, timedelta
from calendar import monthrange
from os import getcwd
from os import path
import pathlib
from shutil import copy

START_DATE = date(2023, 1, 1)
TODAY = date.today()
MONTH = TODAY.month
YEAR = TODAY.year

PROJECTS = {
    'Dungeon': 'Level',
}


def date_range(start, end):
    for n in range(int((end - start).days) + 1):
        yield START_DATE + timedelta(n)


def get_month(date_string):
    return date_string.month


def validate_dirs(outer_dir, prefix):
    dir_path = path.join(getcwd(), outer_dir)

    if not path.exists(dir_path):
        if not path.isdir(dir_path):
            pathlib.Path(dir_path).mkdir(exist_ok=True)
            write_file(dir_path, 'README.md', '')

    for i in range(1, MONTH + 1):
        dir_name = prefix + '_' + f'{i:02}'
        dir_path = path.join(getcwd(),  path.join(outer_dir, dir_name))

        if not path.exists(dir_path):
            if not path.isdir(dir_path):
                pathlib.Path(dir_path).mkdir(exist_ok=True)
                write_file(dir_path, 'README.md', '')


def write_file(file_path, name, content):
    file_path = path.join(getcwd(), path.join(file_path, name))

    if not path.exists(file_path):
        with open(file_path,  'w') as f:
            f.writelines(content)


def validate_files(project, month):
    if month == MONTH:
        day_count = TODAY.day + 1
    else:
        day_count = monthrange(YEAR, month)[1] + 1

    for day in range(1, day_count):
        file_name = path.join('Level_' + f'{month:02}', 'Room_' + f'{day:02}' + '.md')
        dir_name = path.join(project, file_name)

        file_path = path.join(getcwd(), dir_name)

        if not path.exists(file_path):
            write_file



for directory in PROJECTS:
#     validate_dirs(directory, PROJECTS[directory])
    validate_files(directory, 5)
#



# for single_date in date_range(START_DATE, END_DATE):
#     get_month(single_date)
#     print(single_date.strftime("%Y-%m-%d"))

# def get_week(self):
#     return int(date(self.today.year, self.today.month, self.today.day).strftime("%U"))

# today = datetime.now()
# month = today.month
# day_number = today.timetuple().tm_yday
#
# print("Today is day:", day_number, "of", today.year)
# print(month)
#
# projects = [
#     'Dungeon',
# ]
#
# for directory in projects:
#     print(directory)