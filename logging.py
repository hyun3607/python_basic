import logging
import os
import sys


def get_logger(name=None):
    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")
    formatter_e = logging.Formatter("%(asctime)s - %(levelname)s - [%(module)s:%(lineno)d] - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S")
    # 시간 - log레벨 - 파일명:에러라인 - 메시지

    console = logging.StreamHandler()


    log_dir = 'D:/python/logs/'+name+'/'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    file_handler_info = logging.FileHandler(filename = log_dir+name+"_info.log")
    file_handler_error = logging.FileHandler(filename = log_dir+name+"_error.log")

    console.setLevel(logging.INFO)
    file_handler_info.setLevel(logging.INFO)
    file_handler_error.setLevel(logging.ERROR)

    console.setFormatter(formatter)
    file_handler_info.setFormatter(formatter)
    file_handler_error.setFormatter(formatter_e)

    logger.addHandler(console)
    logger.addHandler(file_handler_info)
    logger.addHandler(file_handler_error)

    return logger