#  Logging
import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# import logger_trial

'''
#read config file 
import logging.config
logging.config.dictConfig('logging.conf')
logger = logging.getLogger('simpleExmaple')
'''

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is warning')
logger.error('this is an error')