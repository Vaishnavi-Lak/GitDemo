import inspect
import logging


class Baseclass:
    def logDemo(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # name is used to mention test case name in object

        filelocation = logging.FileHandler("logfile.txt")  # create an object to specify the location of file

        formatting = logging.Formatter("%(asctime)s  :%(levelname)s  : %(name)s  :%(message)s")
        filelocation.setFormatter(formatting)

        logger.addHandler(filelocation)  # pass the location through created object
        logger.setLevel(logging.DEBUG)
        return logger
