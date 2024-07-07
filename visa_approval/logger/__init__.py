import logging
import os

from from_root import from_root
from datetime import datetime

#logging strings
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#log folder name
log_dir = "logs"
#create log file inside log folder
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)
os.mkdir(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    # time of code exicute, file name, level name and message you want to save
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)