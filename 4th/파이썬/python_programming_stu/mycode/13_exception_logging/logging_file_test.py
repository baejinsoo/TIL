import logging


def say_hello(msg):
    return 'Hello ' + msg


# logger 생성
root_logger = logging.getLogger()
# 로그 레벨 설정
root_logger.setLevel(logging.DEBUG)
# 로거 파일 핸들러 생성 (만들 파일이름, 읽고쓰기 선택, 영어이외의 언어 한글파일 넣고 싶으면 utf-8)
fileHandler = logging.FileHandler('test.log', 'w', 'utf-8')

# 로거 콘솔 핸들러 생성
streamHandler = logging.StreamHandler()


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s %(message)s')

# 파일 핸들러에 파일 포매터를 설정
fileHandler.setFormatter(file_formatter)
streamHandler.setFormatter(formatter)

# 로거 객체에 만든 파일핸들러와 스트림(콘솔)핸들러 등록
root_logger.addHandler(fileHandler)
root_logger.addHandler(streamHandler)

root_logger.debug('Start of Program')
root_logger.debug(say_hello('디버그 모드'))
root_logger.info(say_hello('인포 모드'))
# root_logger.warn(say_hello('warn 모드'))
root_logger.error(say_hello('error 모드'))
root_logger.fatal(say_hello('fatal 모드'))
root_logger.debug('END of Program')
