import logging


def say_hello(msg):
    return 'Hello' + msg


# logging 설정
logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
logging.debug(say_hello('디버그 모드'))
logging.info(say_hello('인포 모드'))
logging.debug('End of program')