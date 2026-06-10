import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.debug)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    