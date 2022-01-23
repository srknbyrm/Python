# python json logger check
import logging
logger = logging.getLogger(__name__)

logger.propagate = False
logger.warning('1')

import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error(f'The Error is {traceback.format_exc()}')

from logging.handlers import RotatingFileHandler

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

from logging.handlers import TimedRotatingFileHandler

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)