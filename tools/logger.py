import logging


class Logger:
    @staticmethod
    def setup_logger(name, log_file, level=logging.INFO):
        """Function to setup as many loggers as you want"""

        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger


# Example usage
if __name__ == "__main__":
    log = Logger.setup_logger('my_logger', 'my_log_file.log')
    log.info("This is an info message")
    log.debug("This is a debug message")
    log.error("This is an error message")
