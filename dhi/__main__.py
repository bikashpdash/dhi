import click
from art import *
import json
from . import app
from .servicer import serve

@click.group()
def cli():
    pass

@click.command()
@click.option('--config', default="config.json", help='Cofig file path')
def start(config):
    tprint("DHI")    
    app.config = app.read_config(config)
    ips=app.config['ip']
    print("Listening to:" , [("%s:%s" % (ip,app.config["port"])) for ip in ips])
    serve(app.config["port"])   


@click.command()
@click.option('--c')
@click.option('--m')
@click.option('--t')
def match(c,m,t):
    from .utils import match_check 
    if t=='s':
        print(match_check.simple_match(c,m))
    if t=='r':
        print(match_check.relevant_match(c,m))
    

@click.command()
@click.option('--message', default="DHI", help='Message')
def echo(message):
    print(message)


if __name__ == '__main__':
    cli.add_command(start)
    cli.add_command(echo)
    cli.add_command(match)
    cli()
