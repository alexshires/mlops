"""
Basic Kafka producer
"""

from typing import Dict
from kafka import KafkaProducer
from pipeline.utils import get_pipeline_config
import logging, json, uuid
from datetime import datetime

logger = logging.getLogger(__name__)
cfg = get_pipeline_config()


def load_data() -> Dict:
    """
    load data from source file for scoring - example pipeline input
    :return:
    """
    data = [{"data": "first"}, {"data": "second"}]
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
        data_point['id'] = str(uuid.uuid4())
        data_point['timestamp'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        print(data_point)
        logger.debug("sending data: %s, type: %s", data_point, type(data_point))
        try:
            future = producer.send(cfg["topics"]["ml-input"], data_point)
        except Exception as e:  # TODO: improve
            logger.error("error - data send failed: %s", e)
