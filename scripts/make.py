import sys
from datetime import datetime, date, timedelta
from calendar import monthrange
from os import getcwd, path, stat
import pathlib

TODAY = datetime.now().timetuple().tm_yday

PROJECTS = [
    'Dungeon',
    'World',
]

BOLD_START = "\033[1m"
BOLD_END = "\033[0;0m"


def validate_files(project_name):
    dir_path = path.join(getcwd(), project_name)

    if not path.exists(dir_path):
        print('{}{}{} does not exist... creating it'.format(BOLD_START, project_name, BOLD_END))
        if not path.isdir(dir_path):
            pathlib.Path(dir_path).mkdir(exist_ok=True)

            print('{}README.md{} does not exist... creating it'.format(BOLD_START, BOLD_END))
            file_path = path.join(dir_path, 'README.md')
            write_file(file_path)

    for day in range(1, TODAY + 1):
        sub_dir_path = path.join(dir_path, get_month(day))

        print(sub_dir_path)

        file_name = f'{day:02}' + '.md'
        dir_name = path.join(project_name, file_name)
        file_path = path.join(getcwd(), dir_name)

        if not path.exists(file_path):
            print('{}{}{} does not exist... creating it'.format(BOLD_START, file_name, BOLD_END))
            write_file(file_path)
        if stat(file_path).st_size == 0:
            print('{}{}{} ... is empty'.format(BOLD_START, file_name, BOLD_END))


def write_file(file_path, content=''):
    if not path.exists(file_path):
        with open(file_path, 'w') as f:
            f.writelines(content)


def get_month(current_day):
    date_object = datetime(datetime.now().year, 1, 1) + timedelta(days=current_day - 1)
    return f'{date_object.strftime("%m"):02}'


def main():

    for directory in PROJECTS:
        validate_files(directory)


if __name__ == '__main__':
    sys.exit(main())