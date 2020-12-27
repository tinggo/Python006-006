import logging
import os.path
import pathlib
import time

def logMe():
    timeLabel = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    logPath = os.path.expanduser('~/logMe.log')
    logPath = pathlib.PurePath(logPath)
    logging.basicConfig(filename=logPath, level=logging.DEBUG, format='%(message)s', filemode='w')
    logging.debug(timeLabel)

if __name__ == '__main__':
    logMe()