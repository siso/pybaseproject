import logging
import logging.config
import logging.handlers
import os

from pybaseproject.colouredconsolehandler import ColouredConsoleHandler

LOGGING_FILE = 'logging.conf'
LOGGING_LEVEL = logging.DEBUG

# LOGGING
if os.path.exists(LOGGING_FILE):
    logging.handlers.ColouredConsoleHandler = ColouredConsoleHandler
    logging.config.fileConfig(LOGGING_FILE)
else:
    logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)
if os.path.exists(LOGGING_FILE):
    logger.debug("found logging configuration file: %s" % LOGGING_FILE)
else:
    logger.debug("cannot find logging configuration file: %s" % LOGGING_FILE)
logging.debug("logging_level: %s" % LOGGING_LEVEL)

