from datetime import datetime, date
from pkgs.city import City
from pkgs.door import Door
from pkgs.room import Room
from pkgs.item import Item
from os import path
from os import getcwd
from shutil import copy


def create_file(project, project_string):
    template_file = path.dirname(path.realpath(__file__)) + project.get_template_path()

    if path.exists(template_file):
        output_file = path.join(getcwd() + project.get_file_path())

        if not path.exists(output_file):
            if project_string is not None:
                with open(template_file, 'r') as f:
                    file_data = f.readlines()

                for index, line in enumerate(file_data):
                    if '{{ CONTENT }}' in line:
                        file_data[index] = line.replace('{{ CONTENT }}', project_string)

                with open(output_file, 'w') as f:
                    f.writelines(file_data)
            else:
                copy(template_file, output_file)

            print(project.get_name() + ' created.')

        else:
            print('SKIPPING: ' + output_file + ' it already exists!')

    else:
        print('ERROR: Template ' + template_file + ' does not exist')


projects = [
    City(),
    Door(),
    Room(),
    Item(),
]

print("Day: ", datetime.now().timetuple().tm_yday, "\n")

for project in projects:
    print('Making ' + project.get_name())
    project_string = project.create()
    create_file(project, project_string)
    print()
