#!/usr/bin/python3.5
#
#
#

import argparse
from lib.again import * 
from lib.againmap import * 
###
# initializing basic logging 
### 

import logging

logging.basicConfig(format  = '%(asctime)s - %(funcName)s - %(levelname)s - %(message)s', 
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    level   = logging.INFO
                    )

logger = logging.getLogger("again")

###
# dealing with cmd arguments
###

parser = argparse.ArgumentParser(
  description='test for again map')
parser.add_argument("-t","--test",help="run test_map")
#parser.add_argument("--host",'-i',    default="raspberry",help="Host default is raspberry")
#parser.add_argument("-p","--port",    default='80',help="Port default is 8181(PlayIt) or 80 classic")
#parser.add_argument("--max_width", type=int,  default=10000,help="Set maximumg width for playback, youtubt_dl only")
parser.add_argument("-d","--debug",   default=False, action='store_true' ,help="enable debug output")


args = parser.parse_args()

if args.debug:
  logger.level=logging.DEBUG

logger.debug('start logging')

again = Again(logger=logger)
again.run_test()


