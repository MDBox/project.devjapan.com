import configparser
import json

config = configparser.ConfigParser()
config.read('.gitmodules')


def read_project(path):
    project = {
        'name': f'{path.split("/", 2)[-1]}',
        'path': f'{path.split("/", 1)[-1]}',
        'url': f'https://project.devjapan.com/{path.split("/", 1)[-1]}',
    }
    return project


projects = []

print(config)
for section in config.sections():
    print(section)
    if section.startswith('submodule'):
        print('Submodule path:', config[section]['path'])
        projects.append(read_project(config[section]['path']))

json.dump(projects, open('docs/projects.json', 'w'), indent=2)