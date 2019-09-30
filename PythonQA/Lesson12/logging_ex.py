import logging
# создаём logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# создаём консольный handler и задаём уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# создаём formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# добавляем formatter в ch
ch.setFormatter(formatter)

# добавляем ch к logger
logger.addHandler(ch)

# код "приложения"
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
