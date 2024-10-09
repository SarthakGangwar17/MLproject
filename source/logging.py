import logging
import os
from datetime import datetime

LogFile=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logPath=os.path.join(os.getcwd(),"logs",LogFile)
os.makedirs=os.path.join(logPath,exit_ok=True)
LogFilePath=os.path.join(logPath,LogFile)

logging.basicConfig(
    filename=LogFilePath,
    format="[%(asctime)s] %(lineno)d %(name)s %(message)s",
    level=logging.INFO,

)



