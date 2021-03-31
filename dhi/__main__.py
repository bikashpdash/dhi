import click
from art import *
import json
from . import helpers
from .servicer import serve


@click.command()
@click.option('--config', default="config.json", help='Cofig file path')
def start(config):
    tprint("DHI")    
    cfg= helpers.read_config(config)
    print(cfg)
    print("Listening to: %s" % cfg["port"]) 
    serve(cfg["port"])   

if __name__ == '__main__':
    start()
