#!/usr/bin/env python

import argparse
import datetime
import time
import utils
from wrfda import wrfda

def obsproc_init(datestart):
    '''
    Initialize WPS timestep
    '''
    WRFDA = wrfda()  # initialize object
    WRFDA.obsproc_init(datestart)


def main(datestring):
    '''
    Main function to initialize WPS timestep:
      - converts cylc timestring to datetime object
      - calls wps_init()
    '''
    dt = utils.convert_cylc_time2(datestring)
    obsproc_init(dt)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Initialize obsproc.')
    parser.add_argument('datestring', metavar='N', type=str,
                        help='Date-time string from cylc suite')
    # parse arguments
    args = parser.parse_args()
    # call main
    main(args.datestring)    
