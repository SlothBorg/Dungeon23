from os import listdir
from os import path
from natsort import natsorted

DIRECTORIES = [
	'Dungeon',
	'Resource',
	'Staircase',
]


def list_files(directory):
	items = natsorted(listdir(directory))
	
	for item in items:
		filepath = path.join(directory, item)

		if path.isdir(filepath):
			list_files(filepath)
		else:
			FILES_LIST.append(filepath)


def filepath_to_link(filepath):
	return '[' + path.basename(filepath) + '](' + filepath + ')'


def write_to_readme(directory):
	if path.exists(path.join(directory, 'README.md')):
		print('README.md exists')


for directory in DIRECTORIES:
	FILES_LIST = []
	list_files(directory)

	write_to_readme(directory)

	for filepath in FILES_LIST:
		print(filepath_to_link(filepath))