import logging

class LogGen:
    """LogGen class that is used to generate logs"""

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="./logs/tests.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m''/%d/%y %H:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
