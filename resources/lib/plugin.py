# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from resources.lib import read
from resources.lib import main
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    data = read.load_url('https://lkg-drehnow.de/wordpress/predigten/')
    arr = main.listOfNewest(data)
    for x in arr:
        listItem = ListItem(path=x.link, label=x.film)
        listItem.setInfo('audio',infoLabels={ 'plot': x.plot })
        listItem.setProperty('IsPlayable', 'true')
        addDirectoryItem(plugin.handle, x.link, listItem)
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
