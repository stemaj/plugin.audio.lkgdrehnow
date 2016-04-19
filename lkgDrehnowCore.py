#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import getUrl
import re

names = []
urls = []

def GetData():

    global names
    global urls

    baseUrl = "http://lkg-drehnow.de/"
    daten = getUrl.getUrll(baseUrl + "predigten.php")

    if not daten[0]:
        return daten[1]

    stringss = daten[0].split("#event\">Predigten besonderer Veranstaltungen");
    strings = stringss[1].split("Rechtsklick");
    strings.pop()

    for str in strings:

        #Datum
        date = re.compile("<p class=\"contenttext\">(.+?)<br/>", re.DOTALL).findall(str)[0]
        prediger = re.compile("<br/><b>(.+?)</b>", re.DOTALL).findall(str)[0]
        thema = re.compile("display: inline;\">(.+?)</h2>", re.DOTALL).findall(str)[0]
        thema = thema.split(" .")
        if (len(thema) > 1):
            ste = thema[1].split(". ")
            if (len(ste) > 1):
                stelle = ste[1]
            if (len(ste) > 2):
                stelle = stelle + " " + ste[2]
                stelle = stelle.strip(" ")
        else:
            stelle = ""
        thema = thema[0]
        thema = thema.strip(" ")
        url = baseUrl + re.compile("<a href=\"(.+?)\">", re.DOTALL).findall(str)[0]
        url = url.replace(" ", "%20")

        names.append(date + " " + prediger + " " + stelle + " " + thema)
        urls.append(url)

#Test:
#GetData()
#http://lkg-drehnow.de/predigten/sonntag/17.04.2016%20-%20Andreas%20Heydrich%20-%20Gott%20will%20uns%20troesten%20(Jahreslosung)%20..........................%20Jesaja%2066,%2010-13.mp3
#i = 0
