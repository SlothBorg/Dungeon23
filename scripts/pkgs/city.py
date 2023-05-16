from datetime import date


class City:

    def __init__(self):
        self.today = date.today()
        self.schedule = [
            'event',
            'faction',
            'lore',
            'person',
            'place',
        ]

    def get_name(self):
        return 'City23'

    def create(self):
        return None

    def get_template_path(self):
        return '/templates/City23/' + self.get_day_to_schedule() + '.md'

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
        return '/City23/District_' + str(f'{self.today.month:02}') + '/' + str(f'{self.today.day:02}') + '_' + self.get_day_to_schedule() + '.md'

    def get_file_dir(self):
        return '/City23/District_' + str(f'{self.today.month:02}' + '/')
