#!/usr/bin/env python

import argparse
import datetime
import time
from wrf import run_wrf
import utils


def main(datestring, interval):
    '''
    Main function to initialize WPS timestep:
      - converts cylc timestring to datetime object
      - calls wrf.__init()
    '''
    dt = utils.convert_cylc_time2(datestring)
    run_wrf(dt, dt + datetime.timedelta(hours=interval))


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Initialize WRF step.')
    parser.add_argument('datestring', metavar='N', type=str,
                        help='Date-time string from cylc suite')
    parser.add_argument('interval', metavar='I', type=int,
			help='Time interval in hours')
   # parse arguments
    args = parser.parse_args()
   # call main
    main(args.datestring, args.interval)   
