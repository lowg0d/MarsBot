import os
import sys
import json

##################################################################

if not os.path.isfile('./mars/config/internal.json'): # check if the internal config exits
    sys.exit() # if not exit
    
else:
    # open the config an save it into a var
    with open('./mars/config/internal.json') as file:
        inter_file = json.load(file)

##################################################################

# function to get a parameter of the config
def get_inter(parameter):
    try:
        response = inter_file[f'{parameter}'] # get the parameter from the config file
        return response # resturn the parameter
    except:
        exit()
