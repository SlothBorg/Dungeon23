from os import listdir
from os import path
import pathlib

DIRECTORIES = [
	'City',
	'Dungeon',
	'Staircase',
]


def list_markdown_files(directory):
	items = listdir(directory)
	items.sort()
	
	for item in items:
		filepath = path.join(directory, item)

		if path.isdir(filepath):
			list_markdown_files(filepath)
		elif directory in DIRECTORIES and filepath == path.join(directory, 'district_readme.md'):
			pass
		elif filepath.endswith('.md'):
			FILES_LIST.append(filepath)


def filepath_to_link(directory, filepath):
	filename = path.basename(filepath)

	if filename == 'district_readme.md' and 'Level' in filepath:
		natural_file_path = pathlib.PurePath(filepath).parent.name.replace(' 0', ' ')

		heading = '\n## ' + natural_file_path + '\n'
		link = '[' + natural_file_path + ' - Overview](' + build_link_from_filepath(directory, filepath) + ')\n'
		return '\n'.join([heading, link])
	else:
		natural_file_path = filepath.replace(' 0', ' ')

		file_name = path.basename(natural_file_path).replace('_0', ' ').replace('_', ' ').strip('.md')
		return '* [' + file_name + '](' + build_link_from_filepath(directory, filepath) + ')'


def build_link_from_filepath(directory, filepath):
	filepath = filepath.replace(directory + '/', '')

	if filepath.endswith('district_readme.md'):
		return filepath.replace('district_readme.md', 'index.html')
	else:
		return filepath.replace('.md', '/index.html')


def write_to_readme(directory, content):
	readme_file = path.join(directory, 'district_readme.md')
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