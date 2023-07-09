# coding=utf-8
import logging
import os
import time


class Logger(object):
    def __init__(self, logger,log_name="Chatqa"):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """

        # 创建一个logger
        self.log_name = log_name
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime('%Y%m%d%H%M', time.localtime())
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_path = os.path.dirname(os.path.abspath(__file__)) + '/message/'
        log_name = log_path + self.log_name+ '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


# if __name__ == '__main__':
#     log = Logger('test','use').getlog()#logger:类型 loggername:日志文件
#     log.info('fox is the best')
#     log.error('fox is the best')