#!/usr/bin/env python
import logging
import os
import sys
from argparse import ArgumentParser

import yaml
from rtmbot import RtmBot


def eprint(str):
    logging.debug(str)


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

    on_heroku = True
    if 'HEROKU_ENV_VAR' in os.environ:
        on_heroku = True
    if on_heroku:
        eprint('on heroku')
        config = {'SLACK_ID': os.environ.get('SLACK_ID', None), 'ALGORITHMIA_KEY': os.environ.get('ALGORITHMIA_KEY', None), 'SLACK_TOKEN': os.environ.get(
            'SLACK_TOKEN', None), 'DEBUG': os.environ.get('DEBUG', None), 'TALK': os.environ.get('TALK', None)}
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
                config = (yaml.load(stream))
                bot = RtmBot(config)
                try:
                    bot.start()
                except KeyboardInterrupt:
                    sys.exit(0)
            except yaml.YAMLError as exc:
                print(exc)
