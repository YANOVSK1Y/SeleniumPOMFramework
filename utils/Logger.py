import logging
import os
import datetime

from utils.SingleTon import SingletonType


class Logger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s] > %(message)s')

        now = datetime.datetime.now()
        dirname = "../log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        self._logger.info('Created logger success')

    def _get_logger(self):
        return self._logger

    @staticmethod
    def debug(msg):
        Logger()._get_logger().debug(msg)

    @staticmethod
    def info(msg):
        Logger()._get_logger().info(msg)

    @staticmethod
    def warning(msg):
        Logger()._get_logger().warning(msg)

    @staticmethod
    def error(msg):
        Logger()._get_logger().error(msg)

    @staticmethod
    def critical(msg):
        Logger()._get_logger().critical(msg)
