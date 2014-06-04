import logging

import pybaseproject
import pybaseproject.bar

logger = logging.getLogger(__name__)

def main():
    print __name__

    bar = pybaseproject.bar.Bar()
    print bar.echo('Hola!')
    logger.debug('debug message')

if __name__ == '__main__':
    main()
