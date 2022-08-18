import os
import sys
import json
import mars.managers.logging_mg as logs 

##################################################################
# check if config exists, if it exits save it in config_file var

if not os.path.isfile('./config.json'):
    logs.out("'config.json' not found! Please add it and try again.", "error")
    sys.exit()
    
else:
    with open('./config.json') as file:
        config_file = json.load(file)

##################################################################
# get config functions

def get(parameter):
    try:
        response = config_file[f'{parameter}'] # get the parameter from the config file
        return response # resturn the parameter
    except:
        logs.out(f'parameter "{parameter}" not in the config.json', 'error')
        exit()

def get_two(parameter1, parameter2):
    try:
        response = config_file[f'{parameter1}'][f'{parameter2}'] # get the parameters from the config file
        return response # resturn the parameters
    except:
        logs.out(f'parameter "{parameter1}.{parameter2}" not in the config.json', 'error')
        exit()

def get_three(parameter1, parameter2, parameter3):
    try:
        response = config_file[f'{parameter1}'][f'{parameter2}'][f'{parameter3}'] # get the parameters from the config file
        return response # resturn the parameters
    except:
        logs.out(f'parameter "{parameter1}.{parameter2}.{parameter3}" not in the config.json', 'error')
        exit()

