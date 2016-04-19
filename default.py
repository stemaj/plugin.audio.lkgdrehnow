#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import socket
import urllib
import lkgDrehnowCore

addonID = 'plugin.audio.lkgdrehnow'
addon = xbmcaddon.Addon(id=addonID)
socket.setdefaulttimeout(30)
pluginhandle = int(sys.argv[1])
translation = addon.getLocalizedString
addonDir = xbmc.translatePath(addon.getAddonInfo('path'))
icon = os.path.join(addonDir ,'icon.png')

def index():
    lkgDrehnowCore.GetData()
    
    names = lkgDrehnowCore.names
    anzahl = len(names)
    urls = lkgDrehnowCore.urls

    for i in range(0, anzahl-1, 1):
        addLink(names[i], urls[i], 'playAudio')
    xbmcplugin.endOfDirectory(pluginhandle)
        
def addLink(name, url, mode):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+urllib.quote_plus(mode)
    liz=xbmcgui.ListItem(name, iconImage="DefaultAudio.png", thumbnailImage=icon)
    liz.setInfo(type="Audio", infoLabels={"Title": name})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def playAudio(url):
    listitem = xbmcgui.ListItem(path= url)
    listitem.setProperty("mimetype", 'audio/mpeg')
    url = xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
    return url

def parameters_string_to_dict(parameters):
	paramDict = {}
	if parameters:
		paramPairs = parameters[1:].split("&")
		for paramsPair in paramPairs:
			paramSplits = paramsPair.split('=')
			if (len(paramSplits)) == 2:
				paramDict[paramSplits[0]] = paramSplits[1]
	return paramDict

params = parameters_string_to_dict(sys.argv[2])
url = urllib.unquote_plus(params.get('url', ''))
mode = urllib.unquote_plus(params.get('mode', ''))

if mode == "playAudio":
    playAudio(url)
else:
    index()
