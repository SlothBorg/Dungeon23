from datetime import datetime, date
from random import choice
from random import randint


class Door:
    material = [
        'Wood', 'Wood', 'Wood', 'Wood', 'Wood',
        'Stone', 'Stone', 'Stone',
        'Brass', 'Brass',
        'Iron',
        'Glass',
        'Bronze',
        'Paper',
        'Cloth',
        'Fire',
        'Fluid',
        'Strands of Beads',
        'Curtain',
        'Bone',
        'Shadow',
        'Dreams',
        'Light',
        'Crystal',
    ]
    descriptor = [
        'Ancient',
        'Stained',
        'Broken',
        "Burnt",
        'Water logged',
        'Shifts and swirls',
        'Actually made of animals',
        'Talking',
        'Demonic',
        'Rusted',
        "Blood splattered",
        "Worn",
        'Battered',
        'Shimmering',
        'Translucent',
        'Gleaming',
        'Polished',
        'Blindingly bright',
        'Sucks air/light/??? out of the area',
        'Icicles',
    ]
    style = [
        'Hidden',
        'Decorative',
        'Double door',
        'Cellar door',
        'Hatch',
        'Trap door',
        'Sliding',
        'Archway',
        'Rolling',
        'Revolving',
        'Barn',
    ]
    feature = [
        'A large padlock',
        'Iron Bars',
        'Large ring serves as the handle',
        'In the shape of an animals face',
        'Is not real',
        'A complex puzzle, is set into the face of the door',
        'Intricately carved',
        "Poorly carved",
        'Covered in graffiti',
        'Gnarled roots protrude from it',
        'A figure is half melded into the door',
        'Featureless to the point, that you are not sure it\'s even there',
    ]

    def __init__(self):
        self.file_path_base = '/Staircase'
        self.day_number = datetime.now().timetuple().tm_yday

    def get_name(self):
        return 'Door'

    def create(self):
        door = '* A: **' + choice(self.style) + '**\n'
        door += '* Made from: **' + choice(self.material) + '**\n'
        door += '* It is: **' + choice(self.descriptor) + '**, **' + choice(self.feature) + '**'
        if randint(0, 1):
            door += '\nThe landing is inhabited!'

        return door

    def get_template_path(self):
        return '/templates/Infinite_Staircase/landing.md'

    def get_file_path(self):
        return self.file_path_base + '/Landing_' + str(date.today().timetuple().tm_yday) + '.md'
