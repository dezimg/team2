# --- RaspberryPi main script --- #

import datetime
import dateutil.praser

# --- import functions --- #
from ./function/time_re.py import time # これどうやってやるん

# -- main function -- #
def main():
    # object
    lect_dat = {}
    result = {}
    # read save file
    while True:
        idm, result['time'] = cardreader()
        result['attendance'] = time(result['time'], lect_dat['time'])
        result['inStudent'] = studentof(idm, lect_dat['students']['idms'])
        # comp(idm:str, students:[str], lect_time:{start:datetime,end:datetime,late:datetime})
        # monitor
        # datawrite()

# -- onexec -- #
if __name__ == '__main__':
    main()
