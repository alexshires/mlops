"""
Wrapper script to run the ML engine
"""

from pipeline.mlengine import consume_and_produce
from pipeline.utils import get_pipeline_config, construct_api
import logging
import json

logger = logging.getLogger(__name__)
config = get_pipeline_config()


if __name__ == "__main__":
    logger.debug("running ML engine")
    consume_and_produce()