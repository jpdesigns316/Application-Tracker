#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/app_tracker/app")

from app import app as application
application.secret_key = 'rF&UM39t6Rn2S6422776H9e3!*5D62*K'
