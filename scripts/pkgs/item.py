from datetime import datetime, date
from random import choice


class Item:
    Theme = [
        'Ancient',
        'Death',
        'Sunken',
        'Love',
        'Empire',
        'Heavy',
        'Rural',
        'Darkness',
        'Bloom',
        'Rust',
        'Noise',
        'Childhood',
        'Time',
        'Excess',
        'Decay',
        'City',
        'Factory',
        'Flood',
        'Sleep',
        'Cold',
        'Ash',
        'Touch',
        'Meat',
        'Solitude',
        'Growth',
        'Greed',
        'Luck',
        'Fall',
        'Pit',
        'Chaos',
        'Laughter',
        'Smoke',
        'Forgotten',
        'Library',
        'Ocean',
        'Song',
        'Roots',
        'Bones',
        'Hangman',
        'Blood',
        'Prophet',
        'Idol',
        'Door',
        'Light',
        'Stars',
        'Bridge',
        'Mask',
        'Cut',
        'Sacrifice',
        'Incense',
        'Rise',
        'Gold',
    ]
    Item = [
        'Armor',
        'Potions',
        'Rings & Jewelry',
        'Books & Scrolls',
        'Staffs',
        'Wands',
        'Weapons',
        'Misc.',
    ]

    def __init__(self):
        self.file_path_base = '/Items'
        self.day_number = datetime.now().timetuple().tm_yday

    def get_name(self):
        return 'Item'

    def create(self):
        item_description = choice(self.Theme) + '\n'
        item_description += choice(self.Item) + '\n'

        return item_description

    def get_template_path(self):
        return '/templates/Items/item.md'

    def get_file_path(self):
        return self.file_path_base + '/Item_' + str(date.today().timetuple().tm_yday) + '.md'
