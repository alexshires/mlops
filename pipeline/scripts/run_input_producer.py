"""
run the producer
"""

from pipeline.input import load_data, send_data
from pipeline.utils import get_pipeline_config
import logging

logger = logging.getLogger(__name__)
cfg = get_pipeline_config()

if __name__ == '__main__':
    logger.debug("running input producer")
    d = load_data()
    send_data(data=d)
