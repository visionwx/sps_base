# -*- coding: utf-8 -*-
import os
import sys
import logging
import logging.handlers

def info(tag, content):
    print("[" + tag + "] " + content)

class MyLogger:
    def __init__(self, logToConsole=True, logFilePath=None, 
        loggerName="LOGGER"):
        self.logToConsole = logToConsole
        self.logFilePath = logFilePath
        self.logCounter = 0
        self.loggerName = loggerName
        self.logger = self.initLogger()
        

    def initLogFolder(self):
        if self.logFilePath is None:
            return
        logFolder = os.path.dirname(self.logFilePath)
        if not(os.path.exists(logFolder)):
            os.makedirs(logFolder)
        return True


    def initLogger(self):
        
        # 获取logger实例，如果参数为空则返回root logger
        logger = logging.getLogger(self.loggerName)

        # 指定logger输出格式
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)-8s: %(message)s')

        # 文件日志, 定义一个RotatingFileHandler，
        # 最多备份5个日志文件，每个日志文件最大10M
        if self.logFilePath is not None:
            # 检查log folder
            self.initLogFolder()
            fileHandler = logging.handlers.RotatingFileHandler(
                self.logFilePath, 
                maxBytes=1024*1024, 
                backupCount=5)
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

        # 控制台日志
        if self.logToConsole:
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.formatter = formatter
            logger.addHandler(consoleHandler)

        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)

        return logger
    

    def info(self, TAG, logContent, withPrint=False):
        content = "[" + TAG + "], " + logContent
        self.logger.info()
        self.logCounter += 1
        if withPrint:
            print(content)
        return True
    

    def warn(self, TAG, logContent, withPrint=False):
        self.logger.warn("[" + TAG + "], " + logContent)
        self.logCounter += 1
        if withPrint:
            print(content)
        return True


    def error(self, TAG, logContent, withPrint=False):
        self.logger.error("[" + TAG + "], " + logContent)
        self.logCounter += 1
        if withPrint:
            print(content)
        return True

LOGGER = None
def getLogger(logToConsole=True, logFilePath=None, 
    logName='LOGGER'):
    global LOGGER
    if LOGGER is not None:
        return LOGGER
    LOGGER = MyLogger(logToConsole, logFilePath, logName)
    LOGGER.info("LOGGER", '{0} logger installed'.format(logName))
    return LOGGER