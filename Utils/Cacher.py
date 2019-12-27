import os

currentPath = os.getcwd()
path = "/mediaFiles/"

try:
    os.mkdir(currentPath + path)
except OSError:
    pass


def cacheMedia(id, media):
    f = open(currentPath + path + id + ".cache", 'w')
    f.write(media)
    f.close()


def getCachedMedia(id):
    try:
        f = open(currentPath + path + id + ".cache", 'r')
        data = f.read()
        f.close()
        return data
    except:
        return None
