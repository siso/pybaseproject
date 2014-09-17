import logging

import pybaseproject
import pybaseproject.bar

logger = logging.getLogger(__name__)

def main():
    print __name__

    bar = pybaseproject.bar.Bar()
    print bar.echo('Hola!')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()
