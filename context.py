# -*- coding: utf-8 -*-

#################################################################################################

import logging
import os
import sys

import xbmc
import xbmcaddon

#################################################################################################

__addon__ = xbmcaddon.Addon(id='plugin.video.jellyfin')
__base__ = xbmc.translatePath(os.path.join(__addon__.getAddonInfo('path'), 'resources', 'lib')).decode('utf-8')
__pcache__ = xbmc.translatePath(os.path.join(__addon__.getAddonInfo('profile'), 'jellyfin')).decode('utf-8')
__cache__ = xbmc.translatePath('special://temp/jellyfin').decode('utf-8')

sys.path.insert(0, __cache__)
sys.path.insert(0, __pcache__)
sys.path.append(__base__)

#################################################################################################

from entrypoint import Context

#################################################################################################

LOG = logging.getLogger("JELLYFIN.context")

#################################################################################################


if __name__ == "__main__":

    LOG.debug("--->[ context ]")

    try:
        Context()
    except Exception as error:
        LOG.exception(error)

    LOG.info("---<[ context ]")
