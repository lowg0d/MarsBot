import os
import sys
import json
import mars.managers.logging_mg as logs 

path = "./mars/DC_PLUGINS"

def create_plugin(name, cat_id, about_id, update_id, version_):
    os.mkdir(f"{path}/{name}")

    aList = {"name": f"{name}",
             "category_id": f"{cat_id}",
             "about_id": f"{about_id}",
             "update_id": f"{update_id}",
             "version": f"{version_}"}
    
    with open(f"{path}/{name}/{name}.json", "w") as outfile:
        json.dump(aList, outfile)    
    outfile.close()

def list_plugins():
    counter = 0
    fl = dict()
    avaible_flights = os.listdir(f"{path}")
    
    for i in avaible_flights:
        counter += 1
        fl[counter] = i
    
    return fl
    
def check_plugin(name):
    
    fl = list_plugins()

    for value in fl.values():
        if str(name) in value:
            return value

def delete_plugin(name):
    os.remove(f"{path}/{name}/{name}.json")
    os.rmdir(f"{path}/{name}/")

##################################################################

def get_from_plugin(parameter, name):
    with open(f'./{path}/{name}/{name}.json') as file:
        config_file = json.load(file)

    response = config_file[f'{parameter}'] # get the parameter from the config file
    return response # resturn the parameter