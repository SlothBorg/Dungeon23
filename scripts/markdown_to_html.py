import markdown
from os import listdir
from os import path

DIRECTORIES = [
	'Dungeon',
]
FILES_LIST = []


def list_markdown_files(directory):
	items = listdir(directory)
	items.sort()
	
	for item in items:
		filepath = path.join(directory, item)

		if path.isdir(filepath):
			list_markdown_files(filepath)
		elif directory in DIRECTORIES and filepath == path.join(directory, 'README.md'):
			pass
		elif filepath.endswith('.md'):
			FILES_LIST.append(filepath)


def markdown_to_html(file_path):
	if path.exists(file_path):
		html_file_path = file_path.replace('.md', '.html')
		
		markdown.markdownFromFile(input=file_path, output=html_file_path)


if __name__ == '__main__':
	for directory in DIRECTORIES:
		list_markdown_files(directory)

		for file in FILES_LIST:
			markdown_to_html(file)