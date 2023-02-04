import os
import re


REGEX = '/\*\*(.*?)\*\*/gm'
DIRECTORIES = [
    'City',
    'Dungeon',
    'Staircase',
]
BOLDED = []

regex = re.compile('/\*\*(.*?)\*\*/gm')

for directory in DIRECTORIES:
    for (root, dirs, files) in os.walk(directory, topdown=True):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r') as file_name:
                    data = file_name.read()
                    matches = re.findall('\*\*(.*?)\*\*', data)

                    BOLDED += list(set(matches))

BOLDED = list(set(BOLDED))

BOLDED.sort()

for tag in BOLDED:
    print(tag)