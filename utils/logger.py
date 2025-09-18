import logging
import os
from datetime import datetime

def setup_logger(name: str = "employee_analyzer", 
                 log_file: str = "employee_analyzer.log",
                 level: int = logging.INFO) -> logging.Logger:
    """Configure and return a logger with file and console handlers"""
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Clear existing handlers to avoid duplicates
    if logger.handlers:
        logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(console_handler)

    
    return logger

logger = setup_logger()