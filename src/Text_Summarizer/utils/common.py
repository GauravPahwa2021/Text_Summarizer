import os
import sys
import yaml
from Text_Summarizer.logging import logger
from Text_Summarizer.exception_handler import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
