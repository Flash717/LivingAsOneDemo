import os.path
from dateutil.parser import parse

from model.picture import picture

def parseDate(dateStr):
    try:
        result = parse(dateStr)
        return result.strftime('%Y-%m-%d')
    except Exception as e:
        print(e)        
    return None

def getDatesFromFile(fileName):
    result = []
    if not os.path.exists(fileName):
        return result
    with open(fileName, 'r') as f:
            line = f.readline().strip()
            while line:
                result.append(line)
                line = f.readline().strip()
    return result

def getLocalImages(config):
    result = []
    picFolder = config.get('PICTURE_FOLDER')
    dateFolders = os.listdir(config.get('PICTURE_FOLDER'))
    for dateFolder in dateFolders:
        pictureList = os.listdir(picFolder + '/' + dateFolder)
        pictureArr = []
        for pic in pictureList:
            pictureArr.append(picture(pic, picFolder + '/' + dateFolder + '/' + pic))
        result.append({
            'date': dateFolder,
            'pictures': pictureArr
        })
    return result

def serialize(obj):
    if isinstance(obj, picture):
        return obj.__dict__

    return obj