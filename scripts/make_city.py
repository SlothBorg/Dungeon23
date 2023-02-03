from datetime import date
from os import path
from os import makedirs
from shutil import copy


SCHEDULE = [
    'event',
    'faction',
    'lore',
    'person',
    'place',
]


def get_day_to_schedule():
    num = DAY - 1

    if num >= len(SCHEDULE):
        tmp_num = num
        while tmp_num >= len(SCHEDULE):
            tmp_num -= len(SCHEDULE)

        return SCHEDULE[tmp_num]
    else:
        return SCHEDULE[num]


def create(template_name):

    template_path = path.dirname(path.realpath(__file__)) + '/templates/City/'
    template_file =  path.join(template_path, template_name + '.md')

    if path.exists(template_file):
        file_dir = 'City/District_' + str(f'{MONTH:02}')

        if not path.isdir(file_dir):
            makedirs(file_dir)
            copy(path.join(template_path, 'district_readme.md'), path.join(file_dir, 'district_readme.md'))

        file_name = str(f'{DAY:02}') + '_' + template_name + '.md'

        copy(template_file, path.join(file_dir, file_name))

        print('Created: \t' + file_name)


TODAY = date.today()
MONTH = TODAY.month
DAY = TODAY.day

create(get_day_to_schedule())
