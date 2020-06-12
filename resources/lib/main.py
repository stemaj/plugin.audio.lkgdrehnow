import re

def getAllFilms(bytes):
    return re.compile("uploads(.+).mp3\"").findall(bytes.decode('utf-8'))

def getAllThema(bytes):
    return re.compile("-title\">(.+)</h3>").findall(bytes.decode('utf-8'))

def getAllMp3(bytes):
    return re.compile("audio/mpeg\" src=\"(.+)\?").findall(bytes.decode('utf-8'))
