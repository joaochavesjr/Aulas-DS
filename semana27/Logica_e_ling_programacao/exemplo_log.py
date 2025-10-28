import logging

# Configure the basic logging settings
# This will output log messages to the console and to a file named 'app.log'
# The level is set to DEBUG, meaning all messages from DEBUG and above will be logged.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler('app.log')  # Output to file
    ]
)

# Get a logger instance
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug('Mensagem de debug (depuração)')
logger.info('Mensagem simples')
logger.warning('Mensagem de alerta.')
logger.error('Mensagem de erro.')
logger.critical('Mensagem de erro crítico.')

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception('An exception occurred!')
