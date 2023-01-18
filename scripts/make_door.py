from random import choice
from random import randint
from datetime import date
from os import path
from os import getcwd

TODAY = date.today().timetuple().tm_yday
MATERIAL = [
    'Wood', 'Wood', 'Wood', 'Wood', 'Wood',
    'Stone', 'Stone', 'Stone',
    'Brass', 'Brass'
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
DESCRIPTOR = [
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
STYLE = [
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
FEATURE = [
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

def create_landing(door_string):
    template_file = path.dirname(path.realpath(__file__)) + '/templates/landing.md'

    if path.exists(template_file):
        new_landing = getcwd() + '/Staircase/Landing_' + str(TODAY) + '.md'

        file_data = []

        with open(template_file, 'r') as f:
            file_data = f.readlines()

        for index, line in enumerate(file_data):
            if '{{ DOOR }}' in line:
                file_data[index] = line.replace('{{ DOOR }}', door_string)

        with open(new_landing, 'w') as f:
            f.writelines(file_data)


def make_door_str():
    door = '* A: **' + choice(STYLE) + '**\n'
    door += '* Made from: **' + choice(MATERIAL) + '**\n'
    door += '* It is: **' + choice(DESCRIPTOR) + '**, **' +choice(FEATURE) + '**'

    return door


print('Creating Landing ' + str(TODAY))

create_landing(make_door_str())

if randint(0, 1):
    print('The landing is inhabited!')

