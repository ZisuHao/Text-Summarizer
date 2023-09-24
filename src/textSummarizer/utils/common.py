import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.

    Parameters
    ----------
    Args:
    ----------path_to_yaml (str) : path like input

    Raises:
    ----------ValueError: if yaml file is empty.
              e: empty file
 

    Returns:
    -------ConfigBox: configBox type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they do not exist.

    Parameters
    ----------
    Args:
    ----------path_to_directories (list) : list of path of directories
    ----------ignore_log (bool,optional) : ignore if multiple dirs is to be created. Defaults to True.

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Parameters
    ----------
    Args:
    ----------path (Path) : path of the file

    Returns:
    -------str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"