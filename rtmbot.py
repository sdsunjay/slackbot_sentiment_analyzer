#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

import yaml
from rtmbot import RtmBot
from __future__ import print_function

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-c',
        '--config',
        help='Full path to config file.',
        metavar='path'
    )
    return parser.parse_args()

# load args with config path
if __name__ == '__main__':
    

    on_heroku = False
    if 'HEROKU_ENV_VAR' in os.environ:
        on_heroku = True
    if on_heroku:
        eprint('on heroku')
	config = {'SLACK_ID': os.getenv('SLACK_ID'), 'ALGORITHMIA_KEY': os.getenv('ALGORITHMIA_KEY'), 'SLACK_TOKEN': os.getenv('SLACK_TOKEN'), 'DEBUG': os.getenv('DEBUG'), 'TALK': os.getenv('TALK')}
        eprint('YAML: ' + str(config))
        eprint(os.environ)        
        bot = RtmBot(config)
        bot.start()
    else:
        if os.path.exists('rtmbot.conf') == False:
	    print('Client secrets file (rtmbot.conf) not found in the app path.')
	    sys.exit(0)
	args = parse_args()
	with open("rtmbot.conf", 'r') as stream:
	    try:
	        print stream
		config = (yaml.load(stream))
                print 'YAML: ' + str(config)
                for x in config:
                    print (x)
#for y in config[x]:
#		        print (y,':',config[x][y])
		    bot = RtmBot(config)
                    try:
                        bot.start()
                    except KeyboardInterrupt:
	                sys.exit(0)
	    except yaml.YAMLError as exc:
	        print(exc)
