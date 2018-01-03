import logging
from os.path import expanduser
import os

logPath = expanduser('~/m1.log')
try:
    os.remove(logPath)
except:
    pass

logging.basicConfig(
        filename = expanduser(logPath),
        level = logging.DEBUG
)
