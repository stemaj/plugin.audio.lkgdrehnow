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
    data = read.load_url('https://lkg-drehnow.de/predigten/')
    arr1 = main.getAllFilms(data)
    arr2 = main.getAllThema(data)
    arr3 = main.getAllMp3(data)

    if len(arr1) == len(arr2) and len(arr2) == len(arr3):
      i = 0
      for x in arr1:
          listItem = ListItem(path=arr3[i], label=arr1[i])
          listItem.setInfo('audio',infoLabels={ 'plot': arr2[i], 'plotoutline': arr2[i] })
          listItem.setProperty('IsPlayable', 'true')
          addDirectoryItem(plugin.handle, arr3[i], listItem)
          i = i+1
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
