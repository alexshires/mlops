"""
Global pipeline utils
"""
from typing import Dict
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=10)
logging.getLogger('kafka').setLevel(20)



def get_pipeline_config(filename: str = "pipeline.json") -> Dict:
    """
    Get global pipeline config - either from file or
    :param filename:
    :return:
    """
    config = {
        "topics": {"ml-input": "ml-input", "ml-output": "ml-output"},
        "apis": {"model": {"url": "localhost", "port": 5000, "route": "score/api"}},
    }
    if filename is not None:
        try:
            with open(filename, "r") as f:
                config = json.load(f)
        except FileNotFoundError:
            logger.error("no file found - returning default configuration")
    return config


def construct_api(api_dict):
    """
    construct and test api
    :param api_dict:
    :return:
    """
    try:
        url = api_dict["url"] if api_dict["url"] else "localhost"
        port = api_dict["port"] if api_dict["port"] else 80
        route = api_dict["route"] if api_dict["route"] else ""
        return f"http://{url}:{port}/{route}"
    except Exception as e:
        logger.error("URL construction failed from %s", api_dict)
        return None
