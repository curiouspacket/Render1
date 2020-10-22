import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Initialize the Jinja2 environment to load templates
# from the current directory
type_device = input('What kind of device would you like to build? (switch, router)')
config_file = input('What is the name of config file? ')
env = Environment(loader=FileSystemLoader('.'))
if type_device == 'switch':
  print('Configuring a Switch...... ')
  template = env.get_template('template_switch-v1.jinja2')
elif type_device == 'router':
  print('Configuring a Router.......')
  template = env.get_template('template_router-v1.jinja2')
else:
  print('Error improper device requested')
#template = env.get_template(sys.argv[1])


# Load the context YAML file into a Python dictionary
with open(config_file, 'r') as datafile:
    context = yaml.load(datafile)
#print(context)


#Create Directory for New Device configs
dirName = 'tempConfigs'
try:
  os.mkdir(dirName)
except:
  print('directory', dirName, 'already exists')


# Render the template and puts the config in a txt file
file_name = config_file
file_name = file_name.replace('yaml', 'txt')
#change the current directory
os.chdir(dirName)
print(os.getcwd())
rendered_template = template.render(**context)
with open(file_name, 'w') as f:
    f.write(rendered_template)
#print(rendered_template)