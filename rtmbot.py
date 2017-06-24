#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

import yaml
from rtmbot import RtmBot


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
    if os.path.exists('rtmbot.conf') == False:
        print('Client secrets file (client_id.json) not found in the app path.')
        exit()
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
