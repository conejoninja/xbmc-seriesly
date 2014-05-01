# -*- coding: iso-8859-1 -*-
#------------------------------------------------------------
# seriesly
# XBMC entry point
# http://blog.tvalacarta.info/plugin-xbmc/seriesly/
#------------------------------------------------------------

# Constants
__plugin__  = "seriesly"
__author__  = "_CONEJO"
__url__     = "http://www.github.com/"
__date__ = "02/03/2014"
__version__ = "1.0.0"

import os
import sys
from core import config
from core import logger

logger.info("[default.py] seriesly init...")

librerias = xbmc.translatePath( os.path.join( config.get_runtime_path(), 'lib' ) )
sys.path.append (librerias)

# Runs xbmc launcher
from platformcode.xbmc import launcher
launcher.run()
