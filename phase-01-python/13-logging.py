import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("User Created")
logging.debug("Debugging Information")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("A critical error occurred")

# Basic logging levels in Python are as follows:
# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50
# If you set the logging level to INFO, it will log messages with levels INFO, WARNING, ERROR, and CRITICAL. Messages with the DEBUG level will not be logged.
# example: logging.basicConfig(level=logging.INFO)

# Don't use root logger everywhere in your code. Instead, create a logger object for each module or class.
# This allows you to have more control over logging and makes it easier to manage logs in larger applications.
logger = logging.getLogger(__name__)

logger.info("User Created")