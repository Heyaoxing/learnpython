
import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    filename='complete.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)


def debug(content):
    logger.debug(content)

def info(content):
    logger.info(content)

def warn(content):
    logger.warn(content)

def error(content):
    logger.error(content)

     