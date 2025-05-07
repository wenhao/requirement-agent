import os
import sys

from loguru import logger


class LogManager:
    def __init__(self, log_dir="logs", debug=False, app_name="requirement_agent"):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.logger = logger
        self.logger.remove()

        level = "DEBUG" if debug else "INFO"

        self.logger.add(
            sys.stdout,
            format="<green>{time:HH:mm:ss}</green> | {level} | {message}",
            colorize=True,
            level=level
        )

        self.logger.add(
            f"{log_dir}/{app_name}.log",
            rotation="100 MB",
            retention="30 days",
            enqueue=True,
            level="DEBUG"
        )


LOG = LogManager(debug=True).logger
