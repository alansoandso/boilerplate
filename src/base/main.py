#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import logging
import requests
import sys

logging.basicConfig(level=logging.INFO, format='%(message)s')


def get_parser():
    parser = argparse.ArgumentParser(description='tool')
    parser.add_argument('--env', action='store', default='quality', help='Set for (integration or production)')
    parser.add_argument('-l', '--list', action='store_true', default=False, help='List all for completion helper')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose')
    parser.add_argument('asset', action="store", nargs='*', help='asset')

    return parser


def command_line_runner(argv=None):
    parser = get_parser()
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        parser.print_usage()
        return

    args = parser.parse_args(argv[1:])

    if args.verbose:
        pass

    # List all
    if args.list:
        print('Kingston\nTwickenham')
        return

    # Do something with this asset
    if args.asset:
        if args.asset[0] == 'Twickenham':
            print(f'Going to :{args.asset}, from: Teddington Hospital Stanley Rd (Stop Q)')
            stop = '490013176S'
        else:
            print(f'Going to :{args.asset}, from: Broad St Stop(E) - For 281 & 33 deduct 2 mins')
            stop = '490004377E'
        arrivals = requests.get('https://api.tfl.gov.uk/StopPoint/' + stop + '/Arrivals').json()
        for bus in arrivals:
            print('Number     : {}'.format(bus.get('lineName')))
            print('Expected at: {}\n'.format(bus.get('expectedArrival').split('T')[1].split('.')[0]))
        return


if __name__ == '__main__':
    sys.exit(command_line_runner())
