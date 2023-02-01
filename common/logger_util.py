'''
Author: 张前薄
Date: 2023-02-01 14:49:31
email: 1915579714@qq.com
FilePath: \pytestDome\common\logger_util.py
'''
import logging
from logging.handlers import RotatingFileHandler
import os

class LogUtil:
    
    # 保存日志信息
    def getlogger(self, logName):
        logger = logging.getLogger(logName)
        # 收集日志级别
        logger.setLevel('INFO')

        # 定义格式
        fmt = '[%(asctime)s]  %(filename)s->{}  line:%(lineno)d  [%(levelname)s]  %(message)s'.format(logName)
        logFormat = logging.Formatter(fmt)
        # 日志写入的路径
        filePath = os.getcwd() + '/log/' + logName
        # 指定日志写入的文件
        fileHandler = RotatingFileHandler(filePath, maxBytes=20*1024*1024, backupCount=10, encoding='utf-8')
        # 日志写入级别
        fileHandler.setLevel('INFO')
        # 指定写入格式
        fileHandler.setFormatter(logFormat)


        # 指定控制台输出的日志
        streamHandler = logging.StreamHandler()
        # 输出日志级别
        streamHandler.setLevel('INFO')
        # 指定输出格式
        streamHandler.setFormatter(logFormat)

        # 添加handler
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)

        return logger

# if __name__ == '__main__':
#     logger = LogUtil().getlogger('case.log')
#     logger.info('hhh')
