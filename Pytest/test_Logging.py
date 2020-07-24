import logging


def test_logDemo():
    logger = logging.getLogger(__name__)  # name is used to mention test case name in object

    filelocation = logging.FileHandler("loggingfile.txt")  # create an object to specify the location of file

    formatting = logging.Formatter("%(asctime)s  :%(levelname)s  : %(name)s  :%(message)s")
    filelocation.setFormatter(formatting)

    logger.addHandler(filelocation)  # pass the location through created object
    logger.setLevel(logging.ERROR)
    logger.debug("Debug statement is printed")
    logger.info("Information for this test case is printed")
    logger.warning("Warning message is printed. But test case execution continues")
    logger.error("Error occurred which is failing the test case")
    logger.critical("Critical error is occurring")
