import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="my.log",level=logging.WARNING,format=LOG_FORMAT)
logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")
s = ["Neo","Matrix","Xirtam","Oen"]
