import logging

logger = logging.getLogger('example_logger')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)
