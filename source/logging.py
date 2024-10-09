import logging
import os
from datetime import datetime

LogFile=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logDir = os.path.join(os.getcwd(), "logs")
os.makedirs(os.path.dirname(logDir),exist_ok=True)
LogFilePath=os.path.join(logDir,LogFile)

logging.basicConfig(
    filename=LogFilePath,
    format="[%(asctime)s] %(lineno)d %(name)s %(message)s",
    level=logging.INFO,

)



