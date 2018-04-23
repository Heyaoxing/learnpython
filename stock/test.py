import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    filename='new.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)
 
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')