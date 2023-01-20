from os import listdir
from os import path
import pathlib
from natsort import natsorted

DIRECTORIES = [
	'Dungeon',
	'Staircase',
]


def list_markdown_files(directory):
	items = natsorted(listdir(directory))
	
	for item in items:
		filepath = path.join(directory, item)

		if path.isdir(filepath):
			list_markdown_files(filepath)
		elif directory in DIRECTORIES and filepath == path.join(directory, 'README.md'):
			pass
		elif filepath.endswith('.md'):
			FILES_LIST.append(filepath)


def filepath_to_link(directory, filepath):
	filename = path.basename(filepath)

	if filename == 'README.md' and 'Level' in filepath:
		heading = '\n## ' + pathlib.PurePath(filepath).parent.name + '\n'
		link = '[' + pathlib.PurePath(filepath).parent.name + ' - Overview](' + build_link_from_filepath(directory, filepath) + ')\n'
		return '\n'.join([heading, link])
	else:
		file_name = path.basename(filepath).replace('_0', ' ').replace('_', ' ').strip('.md')
		return '* [' + file_name + '](' + build_link_from_filepath(directory, filepath) + ')'


def build_link_from_filepath(directory, filepath):
	filepath = filepath.replace(directory + '/', '')

	if filepath.endswith('README.md'):
		return filepath.replace('README.md', '/index.html')
	else:
		return filepath.replace('.md', '/index.html')


def write_to_readme(directory, content):
	readme_file = path.join(directory, 'README.md')
	if path.exists(readme_file):
		file_data = []

		with open(readme_file, 'r') as f:
			file_data = f.readlines()

		for index, line in enumerate(file_data):
			if '{{ INDEX }}' in line:
				content_string = '\n'.join(content)
				file_data[index] = line.replace('{{ INDEX }}', content_string.lstrip())

		with open(readme_file, 'w') as f:
			f.writelines(file_data)


for directory in DIRECTORIES:
	FILES_LIST = []
	list_markdown_files(directory)

	INDEX_CONTENT = []
	for filepath in FILES_LIST:
		INDEX_CONTENT.append(filepath_to_link(directory, filepath))

	write_to_readme(directory, INDEX_CONTENT)