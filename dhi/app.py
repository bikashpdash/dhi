import json

config=None
def read_config(file):
    """ Reading Configuration File"""
    with open(file,'r') as f:
        cfig=json.loads(f.read())
        f.close()
    return  cfig


