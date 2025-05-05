import sys

from loguru import logger


class LogManager:
    def __init__(self, app_name="requirement_agent"):
        self.logger = logger
        self.logger.remove()

        self.logger.add(
            sys.stderr,
            format="<green>{time:HH:mm:ss}</green> | {level} | {message}",
            colorize=True
        )

        self.logger.add(
            f"logs/{app_name}.log",
            rotation="100 MB",
            retention="30 days",
            enqueue=True
        )


LOG = LogManager("requirement_agent").logger
