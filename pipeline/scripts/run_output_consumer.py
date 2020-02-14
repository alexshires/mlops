"""
run the output consumer
"""

from pipeline.output import read_output
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.debug("running output consumer")
    read_output()
