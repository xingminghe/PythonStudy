import logging
LOG_FORMATE = "%(asctime)s-%(levelname)s-%(message)s"
logging.basicConfig(filename="mylog.log",format=LOG_FORMATE,level=logging.WARNING)
logging.debug("This is a debug message!")
logging.info("This is a info message!")
logging.warning("This is a warning message!")
logging.error("This is a error message!")
logging.critical("This is a critical message!")

