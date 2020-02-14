"""
Basic Kafka producer
"""

from typing import Dict
from kafka import KafkaProducer
from pipeline.utils import get_pipeline_config
import logging, json

logger = logging.getLogger(__name__)
cfg = get_pipeline_config()

# load data
def load_data() -> Dict:
    """
    load data from source file for scoring - example pipeline input
    :return:
    """
    data = {"one": "one", "two": "two"}
    return data


def send_data(data: Dict) -> None:
    """
    Send data to topic - taken from global config file
    :param data:
    :return:
    """
    producer = KafkaProducer(
        retries=5, value_serializer=lambda m: json.dumps(m).encode("ascii")
    )
    # Asynchronous by default
    for data_point in data:
        try:
            future = producer.send(cfg["topics"]["ml-input"], data_point)
        except Exception as e:  # TODO: improve
            logger.error("error - data send failed: %s", e)
