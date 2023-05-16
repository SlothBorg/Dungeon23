import sys
from datetime import date, timedelta
from calendar import monthrange
from os import getcwd, path, stat
import pathlib

START_DATE = date(2023, 1, 1)
TODAY = date.today()
MONTH = TODAY.month
YEAR = TODAY.year

PROJECTS = {
    'Dungeon': 'Level',
}

BOLD_START = "\033[1m"
BOLD_END = "\033[0;0m"


def date_range(start, end):
    for n in range(int((end - start).days) + 1):
        yield START_DATE + timedelta(n)


def validate_dirs(outer_dir, prefix):
    dir_path = path.join(getcwd(), outer_dir)

    if not path.exists(dir_path):
        print('{}{}{} does not exist... creating it'.format(BOLD_START, outer_dir, BOLD_END))
        if not path.isdir(dir_path):
            pathlib.Path(dir_path).mkdir(exist_ok=True)

            file_path = path.join(dir_path, 'README.md')
            write_file(file_path)

    for i in range(1, MONTH + 1):
        dir_name = prefix + '_' + f'{i:02}'
        dir_path = path.join(getcwd(),  path.join(outer_dir, dir_name))

        if not path.exists(dir_path):
            print('{}{}{} does not exist... creating it'.format(BOLD_START, dir_name, BOLD_END))
            if not path.isdir(dir_path):
                pathlib.Path(dir_path).mkdir(exist_ok=True)

                file_path = path.join(dir_path, 'README.md')
                write_file(file_path)


def write_file(file_path, content=''):
    if not path.exists(file_path):
        with open(file_path, 'w') as f:
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
            write_file(file_path)
        elif stat(file_path).st_size == 0:
            print('{} ... is empty'.format(file_name))



def main():
    month = 0
    for single_date in date_range(START_DATE, TODAY):
        for directory in PROJECTS:
            validate_dirs(directory, PROJECTS[directory])

        if single_date.month != month:
            month = single_date.month
            validate_files(directory, month)


if __name__ == '__main__':
    sys.exit(main())